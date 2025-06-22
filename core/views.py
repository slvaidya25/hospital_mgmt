from rest_framework import viewsets
from .models import Doctor, Patient, Appointment, Product, Inventory, Prescription, PrescriptionItem
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, ProductSerializer, InventorySerializer, PrescriptionSerializer, PrescriptionItemSerializer

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionItemViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemSerializer
