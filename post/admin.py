from django.contrib import admin
from models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')


admin.site.regsiter(Post, PostAdmin)
