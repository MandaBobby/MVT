from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail 
from django.contrib.auth import authenticate, login
import random


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render('success')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def  success_view(request):
    return render(request, 'success.html')




def increment(request):
    value_store, created = ValuesStore.objects.get_or_create(id=1)
    initial_value = value_store.value
    
    if request.method == 'POST':
        form = ValueForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data['input_value']
            if 'increment' in request.POST:
                value_store.value += input_value
            elif 'decrement' in request.POST:
                value_store.value -= input_value
            value_store.save()
            return redirect('increment')
    else:
        form = ValueForm()
    
    context = {
        'form': form,
        'current_value': value_store.value,
    }
    return render(request, 'increment.html', context)


def registrationForm(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          firstname = request.POST['firstname']
          lastname = request.POST['lastname']
          email = request.POST['email']
          password = request.POST['password']
          confirm_password = request.POST['confirm_password']
          if password == confirm_password:
              member = Registration(firstname=firstname, lastname=lastname, email=email,password=password)
              member.save()    
              return redirect('loginForm')
          else:
              messages.info(request, "Passwords do not match.")
    else:
        form = RegistrationForm()
    return render(request,'registrationForm.html',{'form':form })

def loginForm(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            try:
                # Filter the Registration model with email and password
                user = Registration.objects.get( email=email, password=password )
                if user:
                    user.save()
                    return redirect("dashboard")
            except Registration.DoesNotExist:
                # Handle the case where the user does not exist
                messages.info(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def dashboard(request):
    return render(request,'dashboard.html')


#Todo-LIST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'list.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    
    context = {
        'form': form
    }
    return render(request, 'update_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    
    context = {'task': task}
    return render(request, 'delete.html',context)

#email send
def send_email_view(request):
    subject = 'Hello from Django!'
    message = 'This is a test email sent via Django.'
    sender = 'bobbymanda056@gmail.com'
    recipient_list = ['nunnavasanthbabu@gmail.com']

    try:
      send_mail(
            subject, 
            message, 
            sender, 
            recipient_list,
            fail_silently=False,
            
        )
      return HttpResponse('Email sent successfully.')
    except Exception as e:
     return HttpResponse(f'An error occurred: {str(e)}',status=500)
    


# Store OTPs in a temporary variable or use Django sessions for production
otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = generate_otp()
        otp_storage[email] = otp

        # Send OTP to email
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            'from@example.com',  # Change to your email settings
            [email],
            fail_silently=False,
        )
        request.session['email'] = email
        return redirect('verify_otp')

    return render(request, 'loginn.html')

def verify_otp_view(request):
    if request.method == 'POST':
        email = request.session.get('email')
        otp = request.POST.get('otp')

        if otp == otp_storage.get(email):
            # user = authenticate(request, username=email)  # Assuming you're using email as username
            # if user:
            #     login(request, user)
                return HttpResponse('Login successful!')
            # else:
            #     return HttpResponse('Authentication failed.')
        else:
            return HttpResponse('Invalid OTP.')
  
    return render(request, 'verify_otp.html')


# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.http import HttpResponse
# import random
# from .forms import RegistrationForm, LoginForm

# # Temporary storage for OTPs
# otp_storage = {}

# def generate_otp():
#     return str(random.randint(100000, 999999))

# def register_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Process registration logic
#             firstname = form.cleaned_data['firstname']
#             lastname = form.cleaned_data['lastname']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            
#             # Here you would typically create a user record in the database
#             # For simplicity, we are skipping that part.

#             # Redirect to login page after successful registration
#             return redirect('login')
#     else:
#         form = RegistrationForm()
    
#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             # Here you would typically check user credentials.
#             # For simplicity, we're assuming credentials are correct.

#             otp = generate_otp()
#             otp_storage[email] = otp

#             # Send OTP to email
#             send_mail(
#                 'Your OTP Code',
#                 f'Your OTP code is {otp}',
#                 'vasanthadinesh73@gmail.com',  # Replace with your email settings
#                 [email],
#                 fail_silently=False,
#             )
#             request.session['email'] = email
#             return redirect('verify_otp')
#     else:
#         form = LoginForm()

#     return render(request, 'loginForm.html', {'form': form})

# def verify_otp_view(request):
#     if request.method == 'POST':
#         email = request.session.get('email')
#         otp = request.POST.get('otp')

#         if otp == otp_storage.get(email):
#             # OTP is correct, proceed with successful login logic
#             return HttpResponse('Login successful!')
#         else:
#             return HttpResponse('Invalid OTP.')

#     return render(request, 'verify_otp.html')

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 form.add_error(None, "Invalid email or password")
#     else:
#         form = LoginForm()
#     return render(request, 'LoginForm.html', {'form': form})

# @login_required
# def dashboard(request):
#     return render(request,'dashboard.html')



import random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import RegistrationForm, LoginForm, ProductForm
from .models import Product, ProductRegistration

# Temporary storage for OTPs
otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))

otp_storage = {}

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('loginn') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

           
            try:
                user = ProductRegistration.objects.get(email=email, password=password)
                request.session['email'] = email
                request.session['role'] = user.role

                otp = str(random.randint(100000, 999999))
                otp_storage[email] = otp

                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}.',
                    'vasanthadinesh73@gmail.com',
                    [email],
                    fail_silently=False,
                )

                return redirect('verify_otp')
            except ProductRegistration.DoesNotExist:
                return HttpResponse('Invalid email or password', status=400)
    else:
        form = LoginForm()
    return render(request, 'loginn.html', {'form': form})

def verify_otp_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('email')
        if otp == otp_storage.get(email):
            role = request.session.get('role')
            if role == 'admin':
                return redirect('admin_dashboard')
            elif role == 'user':
                return redirect('user_dashboard')
        return HttpResponse('Invalid OTP', status=400)
    return render(request, 'verify_otp.html')

def admin_dashboard_view(request):
    if 'email' not in request.session or request.session.get('role') != 'admin':
        return redirect('login')
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'admin_dashboard.html', {
        'form': form,
        'product_data_list': products
    })

def update_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form})

def delete_product_view(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('admin_dashboard')

from django.shortcuts import render, redirect
from .models import Product

def user_dashboard_view(request):
    # Ensure user is logged in and has 'user' role
    if request.session.get('role') != 'user':
        return redirect('login')
    
    # Retrieve all products
    products = Product.objects.all()
    return render(request, 'user_dashboard.html', {
        'product_data_list': products
    })
from django.shortcuts import redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse

def buy_product_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        buy_quantity = int(request.POST.get('buy_quantity', 0))

        product = get_object_or_404(Product, id=product_id)

        if 0 < buy_quantity <= product.quantity:
            product.quantity -= buy_quantity
            product.save()
            return redirect('user_dashboard')
        return HttpResponse('Invalid quantity', status=400)

    return HttpResponse('Invalid request',status=400)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/admin/')
        else:
            return HttpResponse('Invalid login details broo')
    return render(request,'loginnn.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SuperuserCreationForm

def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_superuser(username=username, email=email, password=password)
            return redirect('/loginnn') 
    else:
        form = SuperuserCreationForm()

    return render(request, 'create_superuser.html',{'form':form})



from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
def create_db(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
         username= request.POST['username']
         email = request.POST['email']
         password = request.POST['password']
         confirm_password = request.POST['confirm_password']
         if password== confirm_password:
             newpassword=make_password(password)  
             RegistrationDatabase.objects.create(username=username,email=email,password=newpassword)
             User.objects.create_superuser(username=username,email=email,password=password)
             return redirect('/admin/')
    else:
      form = RegisterForm()
    return render(request, 'register.html', {'form': form})


