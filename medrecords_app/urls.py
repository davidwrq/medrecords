from django.conf.urls import url
from django.urls import path

from medrecords_app.views import MedicalRecordView, MedicalRecordCreateView

app_name = "medrecords_app"
urlpatterns = [
    url("", MedicalRecordView.as_view(), name="medical_record"),
    url("record_create/", MedicalRecordCreateView.as_view(), name="medrecord_form"),
]
