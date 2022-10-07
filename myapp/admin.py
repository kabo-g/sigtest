from django.contrib import admin
from . models import Signature
# Register your models here.

class SignatureAdmin(admin.ModelAdmin):

    list_display = ["firstname", "lastname", "email"]


admin.site.register(Signature, SignatureAdmin)
