from django.contrib import admin
from django.contrib.auth.models import User

from api.models import ToDo


admin.site.register(User)
admin.site.register(ToDo)
