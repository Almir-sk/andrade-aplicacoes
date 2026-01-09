from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/<str:id_projeto>/', views.detalhes_projetos, name='detalhes_projetos'),
]