from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView
from django.apps import apps

from .models import Salon, Mutfak, KucukOda, YatakOda, Tuvalet


class ListRoomsView(View):
    def get(self, request):
        model_names = []
        room_models = apps.get_app_config('rooms').get_models()
        for model in room_models:
            model_names.append(model.__name__)

        context = {
            "rooms": model_names,
        }
        return render(request, "koridor.html", context)


class SalonView(ListView):
    model = Salon
    template_name = 'rooms/salon.html'
    context_object_name = "items"


class MutfakView(ListView):
    model = Mutfak
    template_name = 'rooms/mutfak.html'
    context_object_name = "items"


class KucukOdaView(ListView):
    model = KucukOda
    template_name = 'rooms/kucukoda.html'
    context_object_name = "items"


class YatakOdaView(ListView):
    model = YatakOda
    template_name = 'rooms/yatakoda.html'
    context_object_name = "items"


class TuvaletView(ListView):
    model = Tuvalet
    template_name = 'rooms/tuvalet.html'
    context_object_name = "items"
