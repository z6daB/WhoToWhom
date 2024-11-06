from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_users/<int:event_id>/', views.create_users, name='create_user'),
    path('purchases/<int:event_id>/', views.purchases, name='purchases'),
    path('create_purchase/<int:event_id>/', views.create_purchase, name='create_purchase')
]
