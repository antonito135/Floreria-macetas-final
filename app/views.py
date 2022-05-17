from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
#SeCCION AGREGAR
def index(request):
    return render(request, 'app/index.html')

def agregar(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
        else:
          datos['mensaje'] = "Codigo ya registrado, intente con uno diferente."
    

    return render(request,'app/productos/agregar.html', datos)

def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente!"
            datos['form'] = formulario
    return render(request,'app/productos/modificar.html', datos)


def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/productos/listar.html',datos)

def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar")

def base(request):
    return render(request,'app/base.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def iniciarsesion(request):
    return render(request, 'app/iniciar-sesion.html')

def quienessomos(request):
    return render(request, 'app/quienes-somos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def suscripcion(request):
    datos = {
        'suscripciones' : SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "suscrito correctamente!"
    return render(request, 'app/suscripcion.html',datos)

def carritocompras(request):
    carritocomprasAll = Carrito.objects.all()
    datos = { 'listaCarrito' : carritocomprasAll }
    if request.method == 'POST':
        productos = Carrito()
        productos.id = request.POST.get('id')
        productos.delete()
    return render(request, 'app/mi-cuenta/carrito-compras.html', datos)

def finalizarcompra(request):
    productosAll = Carrito.objects.all()
    if request.method == 'POST':
        productosAll.delete()
    return render(request, 'app/mi-cuenta/finalizar.compra.html')
    
def historialcompras(request):
    return render(request, 'app/mi-cuenta/historial-compras.html')

def menuingresado(request):
    return render(request, 'app/mi-cuenta/menu-ingresado.html')

def miscompras(request):
    return render(request, 'app/mi-cuenta/mis-compras.html')

def misdirecciones(request):
    return render(request, 'app/mi-cuenta/mis-direcciones.html')

def modificardatos(request):
    return render(request, 'app/mi-cuenta/modificar-datos.html')

def registro(request):
    return render(request, 'app/mi-cuenta/registro.html')

def flores(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('nombre')
        prod.precio = request.POST.get('precio')
        prod.imagen = request.POST.get('imagen')

        prod.save()


    return render(request, 'app/tienda/flores.html',datos)


def maceteros(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('nombre')
        prod.precio = request.POST.get('precio')
        prod.imagen = request.POST.get('imagen')

        prod.save()
    
    return render(request, 'app/tienda/maceteros.html',datos)

def arbustos(request):
    productosAll = Producto.objects.all()
    datos = { 
        'listaProductos' : productosAll 
    }

    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('nombre')
        prod.precio = request.POST.get('precio')
        prod.imagen = request.POST.get('imagen')

        prod.save()

    return render(request, 'app/tienda/arbustos.html', datos)

def tierradehoja(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        prod = Carrito()
        prod.nombre = request.POST.get('nombre')
        prod.precio = request.POST.get('precio')
        prod.imagen = request.POST.get('imagen')

        prod.save()

    return render(request, 'app/tienda/tierra-de-hoja.html',datos)



#administrador

def agregarusuario(request):
    datos = {
        'user' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario agregado correctamente!"
        else:
          datos['mensaje'] = "Codigo ya registrado, intente con uno diferente."
    return render(request,'app/usuario/agregar_usuario.html', datos)

def modificarusuario(request, codigo):
    producto = Usuario.objects.get(codigo=codigo)
    datos = {
        'user' : UsuarioForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario modificado correctamente!"
            datos['user'] = formulario
    return render(request,'app/usuario/modificar_usuario.html', datos)


def listarusuario(request):
    UsuariosAll = Usuario.objects.all()
    datos = {
        'listaUsuario' : UsuariosAll
    }
    return render(request,'app/usuario/listar_usuario.html',datos)


def eliminarusuario(request, codigo):
    producto = Usuario.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarusuario")

def seguimiento(request):
    return render(request, 'app/mi-cuenta/seguimiento.html')
    
def listarhistorial(request):
    SeguimientoAll = Seguimiento.objects.all()
    datos = {
        'listaHistorial' : SeguimientoAll
    }
    return render(request, 'app/mi-cuenta/historial-compras.html',datos)

def productosindex(request):
    return render(request, 'app/productos/productos-index.html')

def usuarioindex(request):
    return render(request, 'app/usuario/usuario_index.html')