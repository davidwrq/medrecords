from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

from django.contrib.auth.models import User

User = get_user_model()

class HomeViewListView(LoginRequiredMixin, ListView):
    template_name = "pages/home.html"
    paginate_by = 1
    queryset = User.objects.all()


    def get_context_data(self, **kwargs):
        context = super(HomeViewListView, self).get_context_data(**kwargs)
        context.update({'users_count': User.objects.all().count()})

        return context
