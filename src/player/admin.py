from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    using = 'default'
    list_display = ('id', 'first_name', 'last_name', 'team', 'login' )
    list_display_links = ('id', 'team', )
    search_fields = ('login', 'first_name',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

admin.site.register(Player, PlayerAdmin)
