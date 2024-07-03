# DJ03_models_BD/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('news/', include('news.urls')),
]
