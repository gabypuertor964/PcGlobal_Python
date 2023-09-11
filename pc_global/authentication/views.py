# Importaciones necesarias
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustonRegistrationForm
from django.views import View
from django.contrib.auth.models import Group

class RegisterView(View):
    template_name = 'register_user.html'
    
    def get(self, request): 
        context = {
            'view':'register',
            'form': CustonRegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):

        # Guardado de los datos obtenidos con el método post
        form = CustonRegistrationForm(request.POST)

        # Validación de los datos
        if form.is_valid():

            # Obteniendo el usuario sin guardar en la base de datos
            user = form.save(commit=False)
            
            # Cifrar la contraseña
            user.set_password(form.cleaned_data['password'])

            # Guardar informacion del usuario en BD
            user.save()

            # Obtener la instacia del grupo a asignar
            group = Group.objects.get(name='cliente')

            # Guardar el usuario con la contraseña cifrada
            user.groups.add(group)

            # Redireccionamiento a la página de login
            return redirect('login')

        context = {
            'view':'register',
            'form': CustonRegistrationForm(),
            'errrors': form.errors
        }
        # Renderizado del template con el formulario y los errores
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):

        #Identificador del nombre de la vista a usar
        context={
            'view':'login'
        }
        return render(request, self.template_name,context)

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin:index')
        else:
            context={
                'view':'login',
                'error':'Credenciales inválidas'
            }
            return render(request, self.template_name, context)
