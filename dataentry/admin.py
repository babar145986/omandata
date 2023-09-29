from django.contrib import admin
from .models import AddRecord
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils.html import format_html

# Register your models here.

admin.site.site_header  =  "Oman Administrator"  
admin.site.site_title  =  "Oman Administrator Login"
admin.site.index_title  =  "Oman Data"

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_no', 'nationality', 'passport_no', 
    				'validity_of_the_medical')
    #list_display_links = ('field1', 'field2')
    # list_filter = ('is_active', 'is_staff', 'is_donor', 'date_joined')
    # search_fields = ('full_name', )
    
    def view_record_button(self, obj):
        # Create a link to the single_record_information view for the specific record
        url = reverse('dataentry:al_razi', args=[str(obj.pk)])
        return format_html('<a class="button" href="javascript:void(0);" onclick="openPrintPreview(\'{}\')">Al Razi</a>', url)
    
    def view_record_button_2(self, obj):
        # Create a link to the single_record_information view for the specific record
        url = reverse('dataentry:noor_ul_ship', args=[str(obj.pk)])
        return format_html('<a class="button" href="javascript:void(0);" onclick="openPrintPreview(\'{}\')">Noor Ul Shipa</a>', url)
    
    def view_record_button_3(self, obj):
        # Create a link to the single_record_information view for the specific record
        url = reverse('dataentry:al_gharbia', args=[str(obj.pk)])
        return format_html('<a class="button" href="javascript:void(0);" onclick="openPrintPreview(\'{}\')">Al Gharbia</a>', url)
    
    def view_record_button_4(self, obj):
        # Create a link to the single_record_information view for the specific record
        url = reverse('dataentry:badr_al_sama', args=[str(obj.pk)])
        return format_html('<a class="button" href="javascript:void(0);" onclick="openPrintPreview(\'{}\')">General</a>', url)
    
    view_record_button.short_description = 'Print 1'
    view_record_button_2.short_description = 'Print 2'
    view_record_button_3.short_description = 'Print 3'
    view_record_button_4.short_description = 'Print 4'
    

    list_display = ('name', 'registration_no', 'nationality', 'passport_no', 
                    'validity_of_the_medical', 'view_record_button', 'view_record_button_2',
                    'view_record_button_3', 'view_record_button_4')

admin.site.register(AddRecord, RecordAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)