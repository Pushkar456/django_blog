from django.contrib import admin

# Register your models here.
from blogPost.models import Post,Comments

admin.site.register((Post,Comments))