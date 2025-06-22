from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, ProductViewSet, InventoryViewSet, PrescriptionViewSet, PrescriptionItemViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'products', ProductViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'prescription-items', PrescriptionItemViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('', include(router.urls)),
    path('contact/', views.contact, name='contact'),
]
