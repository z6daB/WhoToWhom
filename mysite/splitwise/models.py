from django.db import models
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()


class Events(models.Model):
    title = models.CharField(max_length=255, unique=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)


class Users(models.Model):
    username = models.CharField(max_length=100, unique=False)
    event = models.ForeignKey(Events, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Expenses(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=255, unique=False)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_expenses', default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    members = models.ManyToManyField(Users, related_name='participated_expenses')

class Debts(models.Model):
    debtor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='debts')
    payer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='debts_creator', default=1)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    purchase = models.ForeignKey(Expenses, on_delete=models.CASCADE, related_name='debts')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='debts')

    @classmethod
    def create_debts_for_members(cls, expense, event):
        total_price = expense.price
        members = expense.members.all()
        num_members = len(members)
        if num_members > 1:
            individual_debt = total_price / num_members

            for member in members:
                if member != expense.creator:  # исключаем создателя расходов, он не должен быть должником
                    cls.objects.create(
                        debtor_id=member,
                        payer_id=expense.creator,
                        debt=individual_debt,
                        purchase_id=expense,
                        event_id=event
                    )