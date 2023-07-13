from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from .forms import SignupForm, ContactInfoForm
from .models import Profile, ContactInfo
from django.contrib.auth.models import User

# XXXXX FRONT XXXXX

def index(request):
    return render(request, 'app/front/main/index.html')

def blog5(request):
    return render(request, 'app/front/main/blog-5.html')

def cart(request):
    return render(request, 'app/front/main/cart.html')

def checkout(request):
    return render(request, 'app/front/main/checkout.html')

def contact(request):
    # contact_info = ContactInfo.objects.first()
    # context = {'contact_info': contact_info}
    return render(request, 'app/front/main/contact.html')

def error404(request):
    return render(request, 'app/front/main/error-404.html')

def lostPassword(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()
        try:
            profile = Profile.objects.get(username=username)
            if profile.email == email:
                user = profile
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                error_message = "Invalid email address."
        except Profile.DoesNotExist:
            error_message = "Invalid username."
        
        return render(request, 'app/front/main/lostPassword.html', {'error_message': error_message})
    else:
        return render(request, 'app/front/main/lostPassword.html')


def productLeftSideBar2(request):
    return render(request, 'app/front/main/products-left-sidebar-2.html')

def productsType1(request):
    return render(request, 'app/front/main/products-type-1.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'member'  # Définir le rôle de l'utilisateur en tant que membre
            user.password=make_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('index')  # Rediriger vers la page d'accueil après l'inscription
            
    else:
        form = SignupForm()
    return render(request, 'app/front/main/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'app/front/main/login.html', {'error_message': error_message})
    else:
        return render(request, 'app/front/main/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def singleBlog1(request):
    return render(request, 'app/front/main/single-blog-1.html')

def trackOrder(request):
    return render(request, 'app/front/main/track-order.html')

# XXXXX BACK XXXXX

def indexBack(request):
    return render(request, 'app/back/main/indexBack.html')

def allUsersBack(request):
    return render(request, 'app/back/main/allUsersBack.html')

def blog5Back(request):
    return render(request, 'app/back/main/blog5Back.html')

# XXXXX CONTACT BACK XXXXX
def contactBack(request):
    # contact_info = ContactInfo.objects.first()
    # context = {'contact_info': contact_info}
    return render(request, 'app/back/main/contactBack.html')

def update_contact_info(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('contactBack')
    else:
        form = ContactInfoForm(instance=contact_info)

    return render(request, 'app/back/main/contactBack.html', {'form': form})

# XXXXX ORDERS BACK XXXXX
def ordersBack(request):
    return render(request, 'app/back/main/ordersBack.html')

def profileBack(request):
    return render(request, 'app/back/main/profileBack.html')

def productLeftSideBar2Back(request):
    return render(request, 'app/back/main/productLeftSideBar2Back.html')

def categoriesBack(request):
    return render(request, 'app/back/main/categoriesBack.html')

