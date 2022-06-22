from django.contrib import admin

from I4G001530SFT import blog
from I4G001530SFT.blog.models import Post

# Register your models here.
admin.site.register(Post)
