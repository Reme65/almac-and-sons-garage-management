from django.shortcuts import render, redirect
from .models import Booking, Customer, Vehicle


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def booking(request):
    vehicle = None
    vehicle_found = False
    lookup_performed = False

    if request.method == "GET" and request.GET.get("lookup_reg"):
        lookup_performed = True
        lookup_reg = request.GET.get("lookup_reg").strip().upper()

        vehicle = Vehicle.objects.filter(
            registration__iexact=lookup_reg
        ).first()

        if vehicle:
            vehicle_found = True

    if request.method == "POST":
        full_name = request.POST.get("name", "").strip()
        name_parts = full_name.split(" ", 1)

        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        registration = request.POST.get("reg", "").strip().upper()
        make = request.POST.get("make", "").strip()
        model = request.POST.get("model", "").strip()
        year = request.POST.get("year", "").strip()

        vehicle = Vehicle.objects.filter(
            registration__iexact=registration
        ).first()

        if vehicle is None:
            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
            )

            vehicle = Vehicle.objects.create(
                customer=customer,
                registration=registration,
                make=make,
                model=model,
                year=year,
            )

        booking = Booking.objects.create(
            vehicle=vehicle,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            vehicle_registration=registration,
            booking_date=request.POST.get("date"),
            service_required=request.POST.get("service"),
        )

        return render(
            request,
            "thank-you.html",
            {"booking": booking},
        )

    return render(
        request,
        "booking.html",
        {
            "vehicle": vehicle,
            "vehicle_found": vehicle_found,
            "lookup_performed": lookup_performed,
        },
    )
    
def thank_you(request):
    return render(request, "thank-you.html")