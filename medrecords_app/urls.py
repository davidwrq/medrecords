from django.conf.urls import url
from django.urls import path

from medrecords_app import views

app_name = "medrecords_app"
urlpatterns = [
    url("record_create/", views.MedicalRecordCreateView.as_view(), name="medrecord_form"),
    url("list", views.MedicalRecordView.as_view(), name="medical_record"),
    url('^record_medical/update/(?P<pk>[\w-]+)$', views.MedicalRecordUpdate.as_view(), name='medrecord_update'),
    url('^record_medical/delete/(?P<pk>[\w-]+)$', views.MedicalRecordDelete.as_view(), name='medrecord_delete'),

]
