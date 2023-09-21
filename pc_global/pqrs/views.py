from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import CreatePqrsForm
from authentication.models import UserCustom
from landing.models import States
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
import random
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class PqrsListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'my_reports.html'
    
    def get_queryset(self):
        return Pqrs.objects.filter(id_cliente=self.request.user).order_by('-id')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Xd"
        return context

class PqrsSearchView(LoginRequiredMixin ,ListView):
    login_url = 'login'
    template_name = 'search.html'
    
    def get_queryset(self):
        return Pqrs.objects.filter(title__icontains=self.query(), id_cliente=self.request.user)
    
    def query(self):
        return self.request.GET.get('query')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        # context['count'] = context['query'].count()
        return context


@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def delete_pqrs(request, id):
    pqrs = Pqrs.objects.get(id = id)
    pqrs.delete()
    messages.success(request, 'Reporte borrado con éxito')
    return redirect('reports')



class PqrsUpdateView(LoginRequiredMixin, SuccessMessageMixin,  UpdateView):
    login_url = 'login'
    model = Pqrs
    form_class = CreatePqrsForm
    template_name = 'update.html'
    success_message = 'Reporte Actualizado con Exito 😉'
    
    def get_success_url(self) -> str:
        return reverse('reports')

@login_required(login_url='http://127.0.0.1:8000/auth/login/')
def CreatePqrs(request):
    
    # aca sacamos los super usuarios
    id_trabajador_consulta = UserCustom.objects.filter(is_superuser=1, is_staff=1)
    
    # aca sacamos aleatoriamente el super usuario o trabajador
    id_trabajador = random.choice(id_trabajador_consulta)
    
    estado = States.objects.get(id=1)

    # initial={'id_trabajador':id_trabajador, 'id_estado':1}
    form = CreatePqrsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        Pqrs = form.save(commit=False)
        
        Pqrs.id_cliente = request.user
        Pqrs.id_trabajador = id_trabajador
        Pqrs.id_estado = estado
        
        Pqrs.save()
        messages.success(request, 'Reporte Creado con Exito')
        return redirect('reports')
    else:
        print('error')

    return render(request, 'createPqrs.html', {'form':form, 'estadoxd':estado})

# redenrizacion del index de adminlte3

def adminlte(request):
    return render(request, 'adminlte3.html')