from django.contrib import admin

# Register your models here.
from ORMapp.models import Restaurent,Sales,Rating,Staff,StaffRestaurent,Order,Product,Comments
from django.contrib.contenttypes.admin import GenericTabularInline

# from django.contrib import admin

class CommentInLine(GenericTabularInline) :
    model=Comments
    max_num=1
class RestaurentAdmin(admin.ModelAdmin) :
    list_display=['id','name']
    inlines=[CommentInLine]
class ModelAdmin(admin.ModelAdmin) :
    list_display=['id','rating']
class CommentAdmin(admin.ModelAdmin) :
    list_display=['text','object_id','content_type','content_object']

admin.site.register(Restaurent,RestaurentAdmin)
admin.site.register(Rating,ModelAdmin)
admin.site.register(Sales)
admin.site.register(Staff)
admin.site.register(StaffRestaurent)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comments,CommentAdmin)
