# Importaciones necesarias
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustonRegistrationForm

class RegisterView(View):
    # Ruta del template de registro (asegúrate de que la ruta esté correcta)
    template_name = 'register_user.html'
    
    def get(self, request, *args, **kwargs):
        form = CustonRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Asumiendo que 'login' es el nombre correcto para la ruta de inicio de sesión en urls.py
        return render(request, self.template_name, {'form': form})
