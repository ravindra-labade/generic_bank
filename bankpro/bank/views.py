
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bank

class Add_bank(CreateView):
    model = Bank
    fields = "__all__"


class List_bank(ListView):
    model = Bank

class Detail_bank(DetailView):
    model = Bank


class Update_bank(UpdateView):
    model = Bank

    fields = "__all__"
    success_url = "/"

class Delete_bank(DeleteView):
    model = Bank
    success_url = "/"
    template_name = "bank/Bank_confirm.html"
