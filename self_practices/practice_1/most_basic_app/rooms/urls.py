from django.urls import path

from .views import SalonView, MutfakView, YatakOdaView, KucukOdaView, TuvaletView, ListRoomsView

urlpatterns = [
    path('', ListRoomsView.as_view(), name='koridor'),
    path('salon', SalonView.as_view(), name='salon'),
    path('mutfak', MutfakView.as_view(), name='mutfak'),
    path('yatakoda', YatakOdaView.as_view(), name='yatakoda'),
    path('kucukoda', KucukOdaView.as_view(), name='kucukoda'),
    path('tuvalet', TuvaletView.as_view(), name='tuvalet'),
    ]

