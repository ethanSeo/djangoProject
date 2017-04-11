from django.contrib import admin
from blog.models import Category, Dongari, Core, Tag

class coreAdmin(admin.ModelAdmin):
    class Meta:
        model = Core
    list_display = ['id', 'name_core', 'kr_name_core']


class categoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
    #qs = Category.objects.all()
    list_display = ['id', 'name_category', 'kr_name_category']


class dongariAdmin(admin.ModelAdmin):
    class Meta:
        model = Dongari
    list_display = ['name_dongari', 'kr_name_dongari', 'category']

admin.site.register(Category, categoryAdmin)
admin.site.register(Dongari, dongariAdmin)
admin.site.register(Core, coreAdmin)

@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    list_display = ['name_tag']


# Register your models here.
