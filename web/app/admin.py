from django.contrib import admin
from django.db import models
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)
