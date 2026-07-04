from django.contrib import admin
from .models import Booking, Customer, Vehicle

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("registration", "make", "model", "year", "customer")
    search_fields = ("registration", "make", "model", "customer__first_name", "customer__last_name")
    list_filter = ("make", "year")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "get_customer",
        "vehicle",
        "vehicle_registration",
        "service_required",
        "booking_date",
        "status",
  )

    search_fields = (
        "first_name",
        "last_name",
        "vehicle_registration",
        "email",
    )

    list_filter = (
        "service_required",
        "status",
        "booking_date",
    )

    list_display = (
        "first_name",
        "last_name",
        "vehicle_registration",
        "vehicle",
        "service_required",
        "booking_date",
        "status",
    )
  
    ordering = ("booking_date",)

def get_customer(self, obj):
    if obj.vehicle and obj.vehicle.customer:
        return obj.vehicle.customer
    return f"{obj.first_name} {obj.last_name}"

    get_customer.short_description = "Customer"   