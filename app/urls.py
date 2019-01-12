from django.urls import path

# import views de?
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('bar', views.bar, name='bar'),
    path('plate', views.plate, name='plate'),
    path('display_form_bar', views.display_form_bar, name='display_form_bar'),
    path('display_form_plate', views.display_form_plate, name='display_form_plate'),
    path('compare_bode_bar', views.compare_bode_bar, name='compare_bode_bar'),
    path('compare_bode_plate', views.compare_bode_plate, name='compare_bode_plate'),
    path('disk', views.disk, name='disk'),
    path('ring', views.ring, name='ring')
]
