import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from django.utils.html import strip_tags
from django.db.models import Q
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.files.base import ContentFile

@login_required(login_url='/login')
def show_main(request):
    context = {
        'tagline': 'anytime. anywhere.',
        'name' : 'Daniel Ferdiansyah',
        'class' : 'PBP F',
        'npm' : '2306275052',
        'login_user' : request.user.username,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    # Use request.FILES to handle uploaded files (like images)
    form = ProductForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        product = form.save(commit=False)  # Create the product instance but don't save yet
        product.user = request.user  # Associate the product with the current user
        product.save()  # Now save the product instance to the database
        return redirect('main:show_main')  # Redirect to the main page after saving

    context = {
        'form': form,
        'name': 'Daniel Ferdiansyah',
        'class': 'PBP F'
    }
    return render(request, "create_product.html", context)
    
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form,
                'name' : 'Daniel Ferdiansyah',
                'class' : 'PBP F'}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form,
               'name' : 'Daniel Ferdiansyah',
               'class' : 'PBP F'}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Product.objects.get(pk=id, user=request.user)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Add request.FILES to handle image
        if form.is_valid():
            form.save()
            return redirect('main:show_main')  # Redirect to the product detail page or wherever necessary
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")
    image = request.FILES.get("image")
    user = request.user
    
    new_product = Product(
        name=name, 
        price=price,
        description=description,
        quantity=quantity,
        image=image,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def product_list(request):
    products = Product.objects.all()
    data = serialize('json', products)
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            # Handle JSON and form data appropriately
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                image_file = None
            else:
                data = request.POST
                image_file = request.FILES.get('image')

            # Fetch the user (adjust as needed if you have specific auth logic)
            user_id = data.get("user_id")
            user = User.objects.get(id=user_id) if user_id else None
            if not user:
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid or missing user ID"
                }, status=400)

            # Create the Product instance
            new_product = Product.objects.create(
                user=user,
                name=data.get("name"),
                price=int(data.get("price")),
                description=data.get("description", ""),
                quantity=int(data.get("quantity", 0)),
                image=image_file,
            )

            # Check if the price is valid
            if not new_product.is_price_valid:
                return JsonResponse({
                    "status": "error",
                    "message": "Price must be greater than 0"
                }, status=400)

            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "User not found"
            }, status=404)
        except KeyError as e:
            return JsonResponse({
                "status": "error",
                "message": f"Missing field: {str(e)}"
            }, status=400)
        except ValueError as e:
            return JsonResponse({
                "status": "error",
                "message": f"Invalid value: {str(e)}"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
