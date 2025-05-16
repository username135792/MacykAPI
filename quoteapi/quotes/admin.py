from django.contrib import admin
from .models import Theme, Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'display_themes')
    filter_horizontal = ('themes',)
    
    def display_themes(self, obj):
        return ", ".join([theme.name for theme in obj.themes.all()])
    display_themes.short_description = 'Themes'

admin.site.register(Theme)
admin.site.register(Quote, QuoteAdmin)