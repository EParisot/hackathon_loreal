from django.urls import path

from . import views

urlpatterns = [
        path('<str:product>', views.index, name='product'),
]
