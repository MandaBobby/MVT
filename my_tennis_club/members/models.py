from django.db import models

class Member(models.Model):
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
   phone = models.IntegerField(null=True)
   joined_date = models.DateField(null=True)

   def __str__(self):
    return f"{self.firstname} {self.lastname}"
   
   from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def _str_(self):
    return f"{self.firstname}"
  

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField() 

    def _str_(self):
        return f'{self.first_name} {self.last_name}'
    
class ValuesStore(models.Model):
       value=models.IntegerField(default=0)


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  

    def _str_(self):
        return self.title
        

class Registration(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)

  def _str_(self):
    return f'{self.firstname}'
  
  from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  
    quality = models.CharField(max_length=100)  
    quantity = models.PositiveIntegerField()  

    def _str_(self):
        return self.name
    
from django.db import models

class ProductRegistration(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User')])

    def _str_(self):
        return f"{self.firstname} {self.lastname}({self.email})"
  

from django.db import models

class RegistrationDatabase (models.Model):
    username = models.CharField(max_length=124)
    email = models.EmailField()
    password = models.CharField(max_length=128)
  