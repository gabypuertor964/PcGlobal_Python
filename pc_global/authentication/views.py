# Importaciones necesarias
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustonRegistrationForm

class RegisterView(View):

    # Impotacion de los formularios
    from . import forms

    # Nombre del template a usar 
    template_name = 'register_user.html'
    
    def get(self, request):

        # Instanciamiento del formulario de registro
        form = CustonRegistrationForm()

        # Renderizado del template con el formulario
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        # Guardado de los datos obtenidos con el metodo post
        form = CustonRegistrationForm(request.POST)

        # Validacion de los datos
        if form.is_valid():

            # Guardado de los datos
            form.save()

            # Redireccionamiento a la pagina de login
            return redirect('login')
        
        # Obtencion de los errores
        errors = form.errors

        # Renderizado del template con el formulario y los errores
        return render(request, self.template_name, {'form': form,'errors':errors})
