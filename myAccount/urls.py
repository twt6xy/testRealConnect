from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account_page, name='account'),
    path('account/reps/', views.rep_page, name='reps')
]