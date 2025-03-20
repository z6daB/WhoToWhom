from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "create_users/<int:event_id>/", views.create_users, name="create_user"
    ),
    path("purchases/<int:event_id>/", views.purchases, name="purchases"),
    path(
        "create_purchase/<int:event_id>/",
        views.create_purchase,
        name="create_purchase",
    ),
    path(
        "analysis/<int:event_id>/<int:expenses_id>/",
        views.analysis,
        name="analysis",
    ),
    path('update_debt/', views.update_debt, name='update_debt'),
]
