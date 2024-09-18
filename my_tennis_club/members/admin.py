from django.contrib import admin
from .models import Member,Contact
from .models import *
# Register your models here.

admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(ProductRegistration)
admin.site.register(Task)
admin.site.register(Registration)
admin.site.register(RegistrationDatabase)