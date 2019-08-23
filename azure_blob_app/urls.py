from django.urls import path
from .views import index, FirstTrail

urlpatterns = [
    path('', index, name='index'),
    path('all/', FirstTrail.as_view()),
]
