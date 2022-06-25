from django.urls import path

from .views import panel, pending, cancelled

urlpatterns = [
    path('', panel),
    path('pending/', pending),
    path('cancelled/', cancelled),
]
