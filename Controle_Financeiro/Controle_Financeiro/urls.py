
from django.contrib import admin
from django.urls import path
from APP_Controle_Financeiro.views import index, register, Do_login, home_aplicacao, nova_transacao, view_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', Do_login, name='login'),
    path('home_aplicacao/', home_aplicacao, name='home_aplicacao'),
    path('nova_transacao/', nova_transacao, name='nova_transacao'),
    path('view_categoria/', view_categoria, name='view_categoria')

]
