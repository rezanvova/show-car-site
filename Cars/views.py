from django.shortcuts import render
from django.views.generic import ListView

from Cars.models import Car
from Cars.utils import DataMixin


class CarsList(DataMixin, ListView):
    template_name = 'cars/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Car.objects.filter(is_published=True)