from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views.generic import ListView, TemplateView, DetailView

from Cars.models import *
from Cars.utils import DataMixin


class CarsList(DataMixin, ListView):
    model = Car
    template_name = 'cars/models.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self):
        return Car.objects.filter(is_published=True).order_by('id')


class About(DataMixin, TemplateView):
    template_name = 'cars/about.html'


class CarsListCategory(DataMixin, ListView):
    model = Car
    template_name = 'cars/models.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


class CarsListTags(DataMixin, ListView):
    model = Car
    template_name = 'cars/models.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Car.objects.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')


class ShowCar(DataMixin, DetailView):
    model = Car
    template_name = 'cars/carpage.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['button_clicked'] = self.request.session.get('button_clicked', False)
        return self.get_mixin_context(context, title=context['car'].description)

    def post(self, request, *args, **kwargs):
        value = request.POST.get('rating')
        if value is not None:
            try:
                result = int(value)
            except ValueError:
                return self.get(request, *args, **kwargs)
            request.session['button_clicked'] = True
            obj = self.get_object()
            obj.rating_count += 1
            obj.popularity += result
            obj.save()
        return self.get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        queryset = Car.objects.filter(is_published=True).select_related('cat').prefetch_related('tags')
        return get_object_or_404(queryset, slug=self.kwargs[self.slug_url_kwarg])


class StartView(DataMixin, TemplateView):
    template_name = "cars/home.html"


class ContactsView(DataMixin, TemplateView):
    template_name = "cars/contacts.html"