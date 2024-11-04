# urls.py
from django.urls import path
from .views import Login, Logout, UsuarioCreate, Usuariodelete, Usuarioedit


urlpatterns = [
    path('registro/', UsuarioCreate.as_view(), name='registro'),
    path('editar/', Usuarioedit.as_view(), name='editar'),
    path('deletar/', Usuariodelete.as_view(), name='deletar'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
