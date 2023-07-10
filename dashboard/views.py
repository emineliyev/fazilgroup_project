from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from dashboard.forms import PhoneCreateForm
from parameters.models import Phone


def index(request):
    return render(request, 'dashboard/index.html')


# PARAMETERS START
#     PHONE START
class PhoneListView(ListView):
    model = Phone
    template_name = 'dashboard/parameters/contacts.html'
    context_object_name = 'phones'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhoneListView, self).get_context_data()
        return context


class PhoneCreateView(SuccessMessageMixin, CreateView):
    form_class = PhoneCreateForm
    template_name = 'dashboard/parameters/addphone.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Telefon nömrəsi uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(PhoneCreateView, self).get_context_data()
        return context


class PhoneUpdateView(SuccessMessageMixin, UpdateView):
    form_class = PhoneCreateForm
    model = Phone
    template_name = 'dashboard/parameters/updatenum.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Telefon nömrəsi uğurla dəyişdirildi!'

    def get_context_data(self, **kwargs):
        context = super(PhoneUpdateView, self).get_context_data()
        return context


def delete_phone(request, phone_id):
    reader = Phone.objects.get(id=phone_id)
    reader.delete()
    messages.success(request, 'Nömrə uğurla silindi!')
    return redirect('dashboard:contacts')

#     PHONE END
# PARAMETERS END