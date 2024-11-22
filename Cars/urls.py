from django.urls import path, include

from Cars.views import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Модели", 'url_name': 'models'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'}
        ]

urlpatterns = [
    path('', StartView.as_view(), name='home'),
    path('models/', CarsList.as_view(), name='models'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactsView.as_view(), name='contact'),
    path('models/<slug:post_slug>', ShowCar.as_view(), name='aboutCar'),
    path('models/category/<slug:cat_slug>', CarsListCategory.as_view(), name='categories'),
    path('models/tag/<slug:tag_slug>', CarsListTags.as_view(), name='categories'),
]
