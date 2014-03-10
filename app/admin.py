from django.contrib import admin
from .models import Code, Prop, Tran

# Register your models here.

admin.site.register(Code)

class PropAdmin(admin.ModelAdmin):
	list_display = ('short_name', 'address', 'city', 'state', 'zip', 'enis_no', 'mgmt_co', 'mgmt_pct')
admin.site.register(Prop, PropAdmin)

class TranAdmin(admin.ModelAdmin):
	list_display = ('prop', 'date', 'code', 'amt')
admin.site.register(Tran, TranAdmin)
