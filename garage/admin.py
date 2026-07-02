from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
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

    ordering = ("booking_date",)