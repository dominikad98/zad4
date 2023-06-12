from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kurs, Uczestnik
from django.urls import re_path

def kurs_detail(request, kurs_id):
    kurs = Kurs.objects.get(id=kurs_id)
    ilosc_uczestnikow = kurs.ilosc_uczestnikow()
    ilosc_miejsc_wolnych = kurs.ilosc_miejsc_wolnych()
    
    context = {
        'kurs': kurs,
        'ilosc_uczestnikow': ilosc_uczestnikow,
        'ilosc_miejsc_wolnych': ilosc_miejsc_wolnych
    }
    
    return render(request, 'kurs_detail.html', context)