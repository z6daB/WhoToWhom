from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CreateEventForm, UserFormSet
from .models import Users, Events


def index(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event = form.save()  # Сохраняем событие и получаем его объект
            return redirect('create_user',
                            event_id=event.id)  # Перенаправляем на create_users с идентификатором события
        else:
            form.add_error(None, 'Ошибка')
    else:
        form = CreateEventForm()

    return render(request, 'splitwise/index.html', context={'form': form})


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
