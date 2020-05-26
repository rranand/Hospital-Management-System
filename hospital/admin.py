from django.contrib import admin
from hospital.models import *
from django.contrib.auth.models import Group


admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(hr)
admin.site.register(reception)
admin.site.register(appointment)
admin.site.register(prescription)
admin.site.register(p_payment)
admin.site.unregister(Group)

admin.site.site_header = "HMS"
admin.site.site_title = "Hospital Management System"
admin.site.index_title = "Welcome to HMS"