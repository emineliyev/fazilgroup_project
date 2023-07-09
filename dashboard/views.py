from django.shortcuts import render
from django.views.generic import ListView, CreateView

from parameters.models import Phone


def index(request):
    return render(request, 'dashboard/index.html')


# PARAMETERS START
#     PHONE START
class PhoneListView(ListView):
    model = Phone
    template_name = 'dashboard/parameters/phone.html'
    context_object_name = 'phones'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhoneListView, self).get_context_data()
        return context


class PhoneCreateView(CreateView):
    pass
#     PHONE END
# PARAMETERS END