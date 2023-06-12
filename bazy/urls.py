from django.contrib import admin
from django.urls import path
from bazyapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurs/<int:kurs_id>/', views.kurs_detail, name='kurs_detail'),
]
