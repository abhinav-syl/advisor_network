from django.contrib import admin

from .models import advisor_name
# Register your models here.
class advisorAdmin(admin.ModelAdmin):

    pass

admin.site.register(advisor_name, advisorAdmin)