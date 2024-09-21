from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CreateEventForm, UserFormSet, ExpenseForm
from .models import Users, Events


def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateEventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)  # Don't save to the database yet
                event.user = request.user  # Set the user to the currently logged-in user
                event.save()  # Now save the event to the database
                return redirect('create_user', event_id=event.id)  # Redirect to create_user with the event ID
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
    event = get_object_or_404(Events, id=event_id)  # Получаем событие по его ID
    if request.method == 'POST':
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)  # Не сохраняем сразу в базу данных
            for instance in instances:
                instance.event = event  # Устанавливаем событие для каждого пользователя
                instance.save()  # Сохраняем пользователя
            return HttpResponse('success')  # Перенаправление после успешного сохранения
    else:
        formset = UserFormSet(queryset=Users.objects.none())  # Пустой набор форм

    return render(request, 'splitwise/create_users.html', {'formset': formset})


def purchases(request):
    return render(request, 'splitwise/purchases/html')


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
            return HttpResponse('Успешно')
    else:
        form = ExpenseForm(event_id=event_id)
    context = {
        'form': form
    }
    return render(request, 'splitwise/add_purchase.html', context=context)
