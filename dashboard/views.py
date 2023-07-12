from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from dashboard.forms import PhoneCreateForm, EmailCreateForm, SocialCreateForm, ParameterCreateForm
from parameters.models import Phone, Email, Social, Parameters


def index(request):
    return render(request, 'dashboard/index.html')


# PARAMETERS START
class ContactsListView(ListView):
    model = Phone
    template_name = 'dashboard/parameters/contacts.html'
    context_object_name = 'phones'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactsListView, self).get_context_data()
        context['emails'] = Email.objects.all()
        context['socials'] = Social.objects.all()
        context['parameters'] = Parameters.objects.all()
        return context


#     PHONE START
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
    success_message = 'Telefon nömrəsi uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(PhoneUpdateView, self).get_context_data()
        return context


def delete_phone(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    phone.delete()
    messages.success(request, 'Nömrə uğurla silindi!')
    return redirect('dashboard:contacts')


#     PHONE END


#     EMAIL START
class EmailCreateView(SuccessMessageMixin, CreateView):
    form_class = EmailCreateForm
    template_name = 'dashboard/parameters/addemail.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'E-mail ünvan uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(EmailCreateView, self).get_context_data()
        return context


class EmailUpdateView(SuccessMessageMixin, UpdateView):
    form_class = EmailCreateForm
    model = Email
    template_name = 'dashboard/parameters/updateemail.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'E-mail ünvanı uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(EmailUpdateView, self).get_context_data()
        return context


def delete_email(request, email_id):
    email = Email.objects.get(id=email_id)
    email.delete()
    messages.success(request, 'Email uğurla silindi!')
    return redirect('dashboard:contacts')
#     EMAIL END


#     SOCIAL START
class SocialCreateView(SuccessMessageMixin, CreateView):
    form_class = SocialCreateForm
    template_name = 'dashboard/parameters/addsocial.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Media uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(SocialCreateView, self).get_context_data()
        return context


class SocialUpdateView(SuccessMessageMixin, UpdateView):
    form_class = SocialCreateForm
    model = Social
    template_name = 'dashboard/parameters/updatemedia.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Media uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(SocialUpdateView, self).get_context_data()
        return context


def delete_media(request, social_id):
    social = Social.objects.get(id=social_id)
    social.delete()
    messages.success(request, 'Media uğurla silindi!')
    return redirect('dashboard:contacts')
#     SOCIAL END


#     PARAMETERS START


class ParameterCreateView(SuccessMessageMixin, CreateView):
    form_class = ParameterCreateForm
    template_name = 'dashboard/parameters/addcontact.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Əlaqə məlumatları əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super(ParameterCreateView, self).get_context_data()
        return context


class ParameterUpdateView(SuccessMessageMixin, UpdateView):
    form_class = ParameterCreateForm
    model = Parameters
    template_name = 'dashboard/parameters/updateparameter.html'
    success_url = reverse_lazy('dashboard:contacts')
    success_message = 'Əlaqə məlumatları uğurla yeniləndi!'

    def get_context_data(self, **kwargs):
        context = super(ParameterUpdateView, self).get_context_data()
        return context


def delete_contact(request, parameter_id):
    social = Parameters.objects.get(id=parameter_id)
    social.delete()
    messages.success(request, 'Əlaqə məlumatı uğurla silindi!')
    return redirect('dashboard:contacts')

#     PARAMETERS END




# PARAMETERS END
