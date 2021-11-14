from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistroFormulario
from apps.usuarios.models import Usuario
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login


def Inicio(request):
	return render(request, 'index.html');
	
@login_required
def Juego(request):
	return render(request, 'juego.html');

def Login(request):
	return render(request, 'usuarios/login.html');

class Registro(CreateView):
    model = Usuario
    form_class = RegistroFormulario
    template_name="usuarios/registro.html"
    success_url = reverse_lazy('inicio')

# def Registro(request):
# 	if request.method == 'POST':
# 		form = RegistroFormulario(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('')
# 	else:
# 		form = RegistroFormulario()
# 	data = {
# 		'form': RegistroFormulario()
# 	}
# 	return render(request, 'usuarios/registro.html', data);