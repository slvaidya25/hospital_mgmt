from django.contrib import admin
from .models import Doctor, Patient, Appointment, Product, Inventory, Prescription, PrescriptionItem
from .forms import PatientForm

class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem
    extra = 3  # show 3 empty form by default

# class PrescriptionAdmin(admin.ModelAdmin):
#     inlines = [PrescriptionItemInline]

class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = ('name', 'dob', 'gender', 'blood_group', 'contact')
    fieldsets = (
        ('Personal Details', {
            'fields': (('name', 'dob', 'gender'), ('contact', 'email', 'blood_group'), ('emergency_contact', 'address'))
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'phone', 'available_from', 'available_to')
    fieldsets = (
        ('Doctor Info', {
            'fields': (('user', 'specialization', 'phone'))
        }),
        ('Availability', {
            'fields': (('available_from', 'available_to'),)
        })
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_time', 'status')
    fieldsets = (
        ('Appointment Details', {
            'fields': (('patient', 'doctor'),)
        }),
        ('Schedule', {
            'fields': (('appointment_time', 'status'),)
        }),
        ('Reason', {
            'fields': ('reason',)
        }),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_prescription_required')
    fieldsets = (
        ('Product Information', {
            'fields': (('name', 'price'),('is_prescription_required', 'description'))
        }),
    )

class PrescriptionAdmin(admin.ModelAdmin):
    inlines = [PrescriptionItemInline]
    list_display = ('patient', 'doctor', 'created_at')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Prescription Details', {
            'fields': (('appointment', 'doctor', 'patient', 'notes'),)
        }),
        # ('Meta', {
        #     'fields': ('created_at',),
        #     'classes': ('collapse',),
        # }),
    )


#admin.site.register(Doctor)
admin.site.register(Patient, PatientAdmin)
#admin.site.register(Appointment)
#admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PrescriptionItem)

