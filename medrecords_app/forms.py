from django.forms import ModelForm

from medrecords_app.models import MedicalRecord

class MedicalRecordCreationForm(ModelForm):


    class Meta:
        model = MedicalRecord
        fields = "__all__"
