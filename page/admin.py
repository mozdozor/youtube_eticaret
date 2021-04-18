from django.contrib import admin
from page.models import Page,Carousel
from django.conf import settings
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=(
        'pk',
        'title',
        'status',
        'updated_at',
    )
    list_filter=(
        'status',
    )
    list_editable=(
        'status',
    )
    list_per_page = settings.LIST_PER_PAGE
    

admin.site.register(Page,PageAdmin)



class CarouselAdmin(admin.ModelAdmin):
    list_display=(
        'pk',
        'title',
        'cover_image',
        'status',
        'updated_at',
    )
    list_filter=(
        'status',
    )
    list_editable=(
        'status',
    )
    
    

admin.site.register(Carousel,CarouselAdmin)