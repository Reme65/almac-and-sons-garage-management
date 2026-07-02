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
    )

    search_fields = (
        "first_name",
        "last_name",
        "vehicle_registration",
    )

    list_filter = (
        "service_required",
        "booking_date",
    )

    ordering = ("booking_date",)