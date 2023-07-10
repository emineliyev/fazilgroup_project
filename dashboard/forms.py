from django import forms
from parameters.models import Phone


# PARAMETERS START
#     PHONE START
class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('phone',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control inputmask', 'data-mask': '(+999)99 999-9999'})
        }
#     PHONE END
# PARAMETERS END