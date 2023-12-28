from django.contrib import admin

# Register your models here.
from .models import BioData, Agreement, Guarantor, MaSt, SEX, ROLE

admin.site.register(MaSt)
admin.site.register(SEX)
admin.site.register(ROLE)

class GuarantorAdmin(admin.ModelAdmin):
    list_display = ("id", "Surname", "Firstname")
admin.site.register(Guarantor, GuarantorAdmin)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ("id", "Name")
admin.site.register(Agreement, AgreementAdmin)
class BioDataAdmin(admin.ModelAdmin):
    list_display = ("id", "Surname", "Firstname")
admin.site.register(BioData, BioDataAdmin)