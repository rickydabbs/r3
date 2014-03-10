from django.contrib import admin
from .models import Code, Prop, Tran

# Register your models here.
admin.site.register(Code)
admin.site.register(Prop)

class TranAdmin(admin.ModelAdmin):
	list_display = ('prop', 'date', 'code', 'amt')
admin.site.register(Tran, TranAdmin)