from django.contrib import admin

from core.models import CloudFunctions, HostProduct , Options

# Register your models here.
admin.site.register(CloudFunctions)
admin.site.register(Options)
admin.site.register(HostProduct)