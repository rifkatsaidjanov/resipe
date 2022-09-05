from django.contrib import admin

from django.contrib import admin
from .models import Recipe, Categorie

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'created_at', 'updated_at', 'is_published') # admin panelga kirganda shu ma'lumotlar ko'rinishi uchun
    list_display_links = ('pk', 'title')    # pk va title xam link bo'ladi
    list_editable = ('is_published', ) # shu joyni o'zida tasdiqlash tugmachasi chiqadi
    list_filter = ('is_published', 'category' ) # admin panelda filter bo'sin (category va is_published bo'yicha)
    search_fields = ('title',) # admin panelda search ochiladi


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Categorie)
