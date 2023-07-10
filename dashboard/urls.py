from django.urls import path

from .views import index, PhoneListView, PhoneCreateView, PhoneUpdateView, delete_phone

app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('contacts/', PhoneListView.as_view(), name='contacts'),
    # PHONE START
    path('addphone/', PhoneCreateView.as_view(), name='addphone'),
    path('deletephone/<int:phone_id>/', delete_phone, name='deletephone'),
    path('number-update/<int:pk>/', PhoneUpdateView.as_view(), name='number-update'),
    # PHONE END
]
