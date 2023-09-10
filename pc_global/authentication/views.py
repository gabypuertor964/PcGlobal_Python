# Importaciones necesarias
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustonRegistrationForm
from django.views import View

class RegisterView(View):
    template_name = 'register_user.html'
    
    def get(self, request):
        form = CustonRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        # Guardado de los datos obtenidos con el método post
        form = CustonRegistrationForm(request.POST)

        # Validación de los datos
        if form.is_valid():

            # Obteniendo el usuario sin guardar en la base de datos
            user = form.save(commit=False)

            # Asigancion de rol de superusuario
            user.is_superuser = True

            # Asignación de permisos para acceso al panel Admin
            user.is_staff = True
            
            # Cifrar la contraseña
            user.set_password(form.cleaned_data['password'])

            # Guardar el usuario con la contraseña cifrada
            user.save()

            # Redireccionamiento a la página de login
            return redirect('login')
        
        # Obtención de los errores
        errors = form.errors

        # Renderizado del template con el formulario y los errores
        return render(request, self.template_name, {'form': form, 'errors': errors})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin:index')
        else:
            # Añade un mensaje de error
            return render(request, self.template_name, {'error': 'Credenciales inválidas'})
