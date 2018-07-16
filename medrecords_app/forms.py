from django import forms

from medrecords_app.models import MedicalRecord

class MedicalRecordCreationForm(forms.ModelForm):


    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MedicalRecordCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
