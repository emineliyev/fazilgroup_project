from django.urls import path

from .views import index, PhoneListView

app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('phone/', PhoneListView.as_view(), name='phone')
]