from django.contrib import admin
from .models import MyUser, WebLinks, Linkcount

# Register your models here.
admin.site.register(MyUser)
admin.site.register(WebLinks)
admin.site.register(Linkcount)
