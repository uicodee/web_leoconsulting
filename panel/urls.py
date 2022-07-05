from django.urls import path

from .views import panel, pending, cancelled, delete, pend, cancel, login

urlpatterns = [
    path('', panel),
    path('login', login),
    path('pending/', pending),
    path('cancelled/', cancelled),
    path('delete/<int:id>', delete),
    path('pending/<int:id>', pend),
    path('cancel/<int:id>', cancel),
]
