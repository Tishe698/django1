import telegram
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Image

# Create your views here.
def index(req):
    return render(req, 'index.html')


def uspeh(req):
    return render(req, 'спасибо_за_обращение.html')


def landing(req):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(req, 'dum/tarif_laiding.html', context)
def korparativ(req):
    return render(req, 'dum/tarif_korparativ_sait.html')
def online_shop(req):
    return render(req, 'dum/online_shop.html')

# Ваше_приложение/views.py






@async_to_sync
async def send_to_telegram(request):
    if request.method == 'POST':
        selected = request.POST.getlist('selected[]')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        project_description = request.POST.get('project_description')

        bot = telegram.Bot(token='6401249910:AAEr0SqhrkLtyC0bXa2A1IIAKlVrsC7eYUo')
        chat_id = '5676333194'

        message = "Выбрано:\n"
        for item in selected:
            message += f"- {item}\n"

        message += f"\nИмя: {name}\n"
        message += f"Номер телефона: {phone}\n"
        message += f"Описание проекта:\n{project_description}"

        await bot.send_message(chat_id=chat_id, text=message)

        return redirect('uspeh')

    else:
        return JsonResponse({'error': 'POST request required'})
