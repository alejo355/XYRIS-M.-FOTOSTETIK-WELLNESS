from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages

# pagina principal , es donde se muestra el logo con el boton que redirecciona al login
def pagina_principal(request):
    return render(request, 'Pagina-Principal/principal.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'Home/inicio.html')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')  
            return render(request, 'Login/login.html')
    else:
        return render(request, 'Login/login.html')

def inicio(request):
    return render(request, 'Home/inicio.html')

