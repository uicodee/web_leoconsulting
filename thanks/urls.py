from django.urls import path

from .views import thanks

urlpatterns = [
    path('', thanks)
]
