from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mis-pagos/', views.pagos_apoderado, name='pagos_apoderado'),

    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
