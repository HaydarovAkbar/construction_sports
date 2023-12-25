from django.http import HttpResponse
from telegram import Update
from .bot.main import bot, dispatcher
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request')

    def post(self, request, *args, **kwargs):
        try:
            body = request.body
            body_json = json.loads(body)
            update: Update = Update.de_json(body_json, bot)
            dispatcher.process_update(update)
        except Exception as e:
            print(e)
        return HttpResponse({'status': True})
