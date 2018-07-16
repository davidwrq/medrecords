from django import forms
from django.contrib.auth import get_user_model


from medrecords_app.models import MedicalRecord

User = get_user_model()


class MedicalRecordCreationForm(forms.ModelForm):


    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MedicalRecordCreationForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(user_type='2')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
