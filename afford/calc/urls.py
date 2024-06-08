from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('calc',views.calc,name='calc'),
    path('even',views.even, name='even'),
    path('prim',views.prim, name='prim'),
]