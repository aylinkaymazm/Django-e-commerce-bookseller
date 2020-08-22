from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile, FAQ


class ContactFormMeassageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','city','country','image_tag']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question','ordernumber', 'answer', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage,ContactFormMeassageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(FAQ, FAQAdmin)