from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib import admin
from medrecords.users.forms import UserChangeForm, UserCreationForm
from medrecords_app.models import MedicalRecord, Medicine, Exam

User = get_user_model()

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name","rut", "user_type")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser", "rut", "user_type"]
    search_fields = ["name"]

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = ["patient"]
    search_fields = ["patient"]

@admin.register(Medicine)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = ["name", "fantasy_name", "type_medicine"]
    search_fields = ["name"]

@admin.register(Exam)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = ["patient", "name"]
    search_fields = ["name"]
