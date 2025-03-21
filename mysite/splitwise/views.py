import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateEventForm, UserFormSet, ExpenseForm
from .models import Users, Events, Expenses, Debts
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateEventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.user = request.user
                event.save()
                return redirect('create_user', event_id=event.id)
            else:
                form.add_error(None, 'Ошибка')
        else:
            form = CreateEventForm()

        events = Events.objects.filter(user_id=request.user.id)
        context = {
            'form': form,
            'events': events
        }
        return render(request, 'splitwise/index.html', context=context)
    else:
        return redirect('accounts/register/')


def create_users(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    if request.method == 'POST':
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.event = event  # Устанавливаем событие для каждого пользователя
                instance.save()
            return redirect('purchases', event_id=event.id)
    else:
        formset = UserFormSet(queryset=Users.objects.none())  # Пустой набор форм

    return render(request, 'splitwise/create_users.html', {'formset': formset})


def purchases(request, event_id):
    objects = Expenses.objects.filter(event_id=event_id)

    context = {
        'objects': objects,
        'event_id': event_id
    }
    return render(request, 'splitwise/purchases.html', context=context)


def create_purchase(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, event_id=event_id)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.event = event
            expense.creator = form.cleaned_data['creator']
            expense.save()
            form.save_m2m()

            Debts.create_debts_for_members(expense, event)

            return redirect('purchases', event_id=event.id)
    else:
        form = ExpenseForm(event_id=event_id)
    context = {
        'form': form
    }
    return render(request, 'splitwise/add_purchase.html', context=context)


@csrf_exempt
def update_debt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            debt_id = data.get('debt_id')
            new_amount = float(data.get('amount'))

            # Проверка на отрицательное значение
            if new_amount < 0:
                return JsonResponse({'status': 'error', 'message': 'Сумма долга не может быть отрицательной'})

            debt = Debts.objects.get(id=debt_id)

            if new_amount == 0:
                debt.delete()
                return JsonResponse({'status': 'deleted', 'message': 'Долг удалён'})

            debt.debt = new_amount
            debt.save()
            return JsonResponse({'status': 'success', 'new_amount': debt.debt})

        except Debts.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Долг не найден'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Неверный запрос'})

def analysis(request, event_id, expenses_id):
    data = Debts.objects.filter(event_id=event_id, purchase_id=expenses_id)
    context = {"data": data}
    return render(request, "splitwise/get_analysis.html", context=context)
