# from django.urls import path
# from . import views

# urlpatterns = [
#   path('', views.index, name='index'),
#   path('add/', views.add, name='add'),
#   path('add/addrecord/', views.addrecord, name='addrecord'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/',views.testing),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('value/', views.increment, name='increment'),

    path('registrationForm/',views.registrationForm ,name='register'),
    path('loginForm/', views.loginForm, name='loginForm'),  # If this is needed separately
    path('dashboard/',views.dashboard,name='dashboard'),

    path('todolist', views.index, name='index'),  
    path('task/update/<int:pk>/', views.update_task, name='update_task'),  
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),

    path('mail/', views.send_email_view, name='mail'), 

    path('register/', views.registration_view, name='register_view'),  # product list
    path('loginn/', views.login_view, name='loginn'),
    path('verify/', views.verify_otp_view, name='verify_otp'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('update_product/<int:id>/', views.update_product_view, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product_view, name='delete_product'),
    path('user_dashboard/', views.user_dashboard_view, name='user_dashboard'),
    path('buy/', views.buy_product_view,name='buy'),

    path('loginnn', views.user_login, name='loginnn'),#admin login

    path('adminuser/', views.create_superuser, name='admin_user'),

    path('encryption', views.create_db, name='passwordencryption')

   
]