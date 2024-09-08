from django.contrib import admin
from .models import Tweet

# Register your models here.

def active_selected_record(self, request, queryset):
    queryset.update(is_active=True)

def inactive_selected_record(self, request, queryset):
    queryset.update(is_active=False)

class TweetAdmin(admin.ModelAdmin):

    list_filter = ['is_active', ]
    search_fields = ['text', ]


    list_display= ['id','admin_photo','user','text','is_active','created_on']

    actions_on_top = True
    actions_on_bottom = True
    empty_value_display = 'NA'
    save_on_top = True

    readonly_fields = ('admin_photo',)

admin.site.add_action(active_selected_record)
admin.site.add_action(inactive_selected_record)

admin.site.register(Tweet, TweetAdmin)