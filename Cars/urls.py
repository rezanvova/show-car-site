from django.urls import path, include

from Cars.views import CarsList
menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Модели", 'url_name': 'models'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'}
        ]


urlpatterns = [
    path('home/', CarsList.as_view(),name='home'),
    path('models/', CarsList.as_view(),name='models'),
    path('about/', CarsList.as_view(),name='about'),
    path('contact/', CarsList.as_view(),name='contact'),
]