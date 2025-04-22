from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Transacao, Categoria



def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        
        if User.objects.filter(email=email).exists():
            return HttpResponseRedirect('/register/?error=User already exists')
        
        
        user = User.objects.create_user(username=username, password=password, email=email)

        user.save()

        return HttpResponseRedirect('/login/?success=User created successfully')
    else:
        return render(request, 'register.html')


def Do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home_aplicacao/')
        else:
            return HttpResponseRedirect('/login/?error=Invalid credentials')
    else:
        return render(request, 'login.html')

@login_required(login_url='/login/')
def nova_transacao(request):
    if request.method == "POST":

        
        
        categoria = request.POST['categoria']
        
        nova_categoria = Categoria.objects.create(nome=categoria, usuario=request.user)
        nova_categoria.save()
        
        
        valor = request.POST['valor']
        tipo = request.POST['tipo']
        descricao = request.POST['descricao']
        data = request.POST['data']
        usuario = request.user 
        nova_transacao = Transacao.objects.create(tipo=tipo, categoria=nova_categoria, valor=valor, descricao=descricao, data=data, usuario=usuario)
        nova_transacao.save()

        
        
        return HttpResponseRedirect('/home_aplicacao/?success=Transação created successfully',)
    
    else:
        return render(request, "aplicacao.html",)
    
@login_required(login_url='/login/')
def home_aplicacao(request):
    if Categoria.objects.filter(usuario=request.user).exists() == 0:
        return HttpResponseRedirect('/nova_transacao/?error=No categories found')
   
    categorias = Categoria.objects.filter(usuario=request.user)

    return render(request, "home_aplicacao.html", {'categorias': categorias})



@login_required(login_url='/login/')
def view_categoria(request):

    view_transacao_user = Transacao.objects.filter(usuario=request.user).first()
    return render(request, "view_categoria.html", {'view_transacao_user': view_transacao_user})