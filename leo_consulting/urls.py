from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('registration.urls')),
    path('thanks/', include('thanks.urls')),
    path('panel/', include('panel.urls')),
]
