from django.shortcuts import render, redirect
from .models import Booking


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def booking(request):
    if request.method == "POST":
        full_name = request.POST.get("name", "")
        name_parts = full_name.split(" ", 1)

        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        Booking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            vehicle_registration=request.POST.get("reg"),
            booking_date=request.POST.get("date"),
            service_required=request.POST.get("service"),
        )

        return redirect("thank_you")

    return render(request, "booking.html")


def thank_you(request):
    return render(request, "thank-you.html")