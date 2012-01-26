from django.contrib import admin
from penncycle.models import Manufacturer, User, Bike, Ride

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'grad_year', 'penncard_number',
        'gender', 'school',)
    search_fields = ('first_name', 'last_name', 'penncard_number',)
    list_filter = ('school', 'gender', 'grad_year')
    date_hierarchy = 'join_date'
    
class BikeAdmin(admin.ModelAdmin):
    list_display = ('bike_name', 'manufacturer', 'purchase_date')
    list_filter = ('purchase_date','manufacturer',)
    date_hierarchy = 'purchase_date'

class RidesAdmin(admin.ModelAdmin):
    list_display = (
        'rider', 'bike', 'checkout_time', 'checkin_time',
        'ride_duration_days',
    )
    list_filter = (
        'rider', 'bike', 'checkout_time', 'checkin_time', 'ride_duration_days',
        'rider',
    ) 
    date_hierarchy = 'checkin_time'
    ordering = ('checkin_time',)
    raw_id_fields = ('bike',)

admin.site.register(Manufacturer)
admin.site.register(User, UserAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Ride, RidesAdmin)
