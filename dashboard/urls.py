from django.urls import path

from .views import index, ContactsListView, PhoneCreateView, PhoneUpdateView, delete_phone, EmailCreateView, \
    EmailUpdateView, delete_email, SocialCreateView, SocialUpdateView, delete_media, ParameterCreateView

app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),

    # PHONE START
    path('add-phone/', PhoneCreateView.as_view(), name='addphone'),
    path('number-update/<int:pk>/', PhoneUpdateView.as_view(), name='numberupdate'),
    path('delete-phone/<int:phone_id>/', delete_phone, name='deletephone'),
    # PHONE END

    # EMAIL START
    path('add-email/', EmailCreateView.as_view(), name='addemail'),
    path('update-email/<int:pk>/', EmailUpdateView.as_view(), name='updateemail'),
    path('delete-email/<int:email_id>/', delete_email, name='deleteemail'),
    # EMAIL END

    # SOCIAL START
    path('add-media/', SocialCreateView.as_view(), name='addsocial'),
    path('update-media/<int:pk>/', SocialUpdateView.as_view(), name='updatesocial'),
    path('delete-media/<int:social_id>/', delete_media, name='deletemedial'),
    # SOCIAL END

    # CONTACT START
    path('add-contact/', ParameterCreateView.as_view(), name='addcontact')
    # CONTACT END
]
