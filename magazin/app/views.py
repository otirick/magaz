from django.shortcuts import render
from .models import *


def index(request):

    if request.method == 'POST':
        print('post')
        return render(request, 'index.html')

    return render(request, 'index.html')

# Выдаём базу и подключаем админку
# 123