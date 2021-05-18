from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:action>', views.process),
    # path('add_ninja', views.add_ninja),
    # path('delete', views.delete),
]
