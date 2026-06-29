from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def booking(request):
    return render(request, "booking.html")


def thank_you(request):
    return render(request, "thank-you.html")