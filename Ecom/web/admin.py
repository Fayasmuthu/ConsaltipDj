from django.contrib import admin

# Register your models here.

from .models import BlogPost ,boxform
from .models import ContactMessage,gallery_photo,ServiceMessage
from .models import Comment



# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'pub_date')
#     filter_horizontal = ('tags',)

admin.site.register(BlogPost)
admin.site.register(ContactMessage)

admin.site.register(gallery_photo)
admin.site.register(ServiceMessage)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'created_at')
    search_fields = ('author', 'email', 'comment')

admin.site.register(boxform)
