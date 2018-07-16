from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.shortcuts import redirect

from medrecords_app.models import MedicalRecord
from medrecords_app.forms import MedicalRecordCreationForm

User = get_user_model()


class HomeViewListView(LoginRequiredMixin, ListView):
    template_name = "pages/home.html"
    paginate_by = 5
    queryset = User.objects.all().exclude(is_superuser=True)

    def get_context_data(self, **kwargs):
        context = super(HomeViewListView, self).get_context_data(**kwargs)
        context.update({'users_count': User.objects.all().exclude(is_superuser=True).count(),
                        'doctor_count':User.objects.filter(user_type=1).count(),
                        'patient_count':User.objects.filter(user_type=2).count()})

        return context


class MedicalRecordView(LoginRequiredMixin, ListView):
    template_name = "pages/medical_records.html"
    paginate_by = 5
    model = MedicalRecord

    def get_queryset(self):
        if self.request.user.user_type == '1':
            return self.model.objects.all()
        else:
            return self.model.objects.filter(patient=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordView, self).get_context_data(**kwargs)

        context.update({'users_count': User.objects.all().exclude(is_superuser=True).count(),
                        'doctor_count':User.objects.filter(user_type=1).count(),
                        'patient_count':User.objects.filter(user_type=2).count()})

        return context


class MedicalRecordCreateView(LoginRequiredMixin, FormView):
    template_name = "pages/medical_record_form.html"
    form_class = MedicalRecordCreationForm
    success_url = reverse_lazy("medrecords:medical_record")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MedicalRecordUpdate(LoginRequiredMixin, UpdateView):
    template_name = "pages/medicalrecord_update_form.html"
    model = MedicalRecord
    form_class = MedicalRecordCreationForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("medrecords:medical_record")


class MedicalRecordDelete(LoginRequiredMixin, DeleteView):
    model = MedicalRecord
    success_url = reverse_lazy("medrecords:medical_record")
