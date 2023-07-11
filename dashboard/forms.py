from django import forms
from parameters.models import Phone, Email, Social, Parameters


# PARAMETERS START
#     PHONE START
class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('phone',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control inputmask', 'data-mask': '(+999) 99 999-99-99'})
        }


#     PHONE END


#     EMAIL START
class EmailCreateForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'uemail', 'name': 'uemail',
                                            'aria-describedby': 'uemail-error', 'aria-invalid': 'true'})
        }


#    EMAIL START


#     SOCIAL START
class SocialCreateForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ('social_name', 'social_icon', 'social_link')
        widgets = {
            'social_name': forms.TextInput(attrs={'class': 'form-control'}),
            'social_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'social_link': forms.TextInput(attrs={'class': 'form-control'}),
        }
#     SOCIAL END


#     PARAMETERS START
class ParameterCreateForm(forms.ModelForm):
    class Meta:
        model = Parameters
        fields = ('address', 'iframe_map', 'phone', 'email', 'social')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'iframe_map': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'email': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'social': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

#     PARAMETERS END

# PARAMETERS END
