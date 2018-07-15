from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView

from medrecords_app.models import MedicalRecord
from medrecords_app.forms import MedicalRecordCreationForm


User = get_user_model()

class HomeViewListView(LoginRequiredMixin, ListView):
    template_name = "pages/home.html"
    paginate_by = 1
    queryset = User.objects.all()


    def get_context_data(self, **kwargs):
        context = super(HomeViewListView, self).get_context_data(**kwargs)
        context.update({'users_count': User.objects.all().count()})

        return context

class MedicalRecordCreateView(LoginRequiredMixin, FormView):
    template_name = "pages/medical_record_form.html"
    form_class = MedicalRecordCreationForm


class MedicalRecordView(LoginRequiredMixin, ListView):
    template_name = "pages/medical_records.html"
    paginate_by = 1
    queryset =  MedicalRecord.objects.all()

