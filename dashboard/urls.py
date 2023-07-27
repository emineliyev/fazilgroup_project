from django.urls import path

from .views import index, ContactsListView, PhoneCreateView, PhoneUpdateView, delete_phone, EmailCreateView, \
    EmailUpdateView, delete_email, SocialCreateView, SocialUpdateView, delete_media, ParameterCreateView, \
    delete_contact, ParameterUpdateView, ProductListView, CategoryListView, CategoryCreateView, delete_category, \
    SubCategoryCreateView, CategoryOrderView

app_name = 'dashboard'
urlpatterns = [
    # PARAMETERS START
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
    path('add-contact/', ParameterCreateView.as_view(), name='addcontact'),
    path('parameter-update/<int:pk>/', ParameterUpdateView.as_view(), name='parameterupdate'),
    path('delete-contact/<int:parameter_id>/', delete_contact, name='deletecontact'),
    # CONTACT END
    # PARAMETERS END

    # PRODUCT START
    path('product-list/', ProductListView.as_view(), name='productlist'),
    path('category-list/', CategoryListView.as_view(), name='categorylist'),
    path('create-category/', CategoryCreateView.as_view(), name='createcategory'),
    path('create-sub-category/', SubCategoryCreateView.as_view(), name='createsubcategory'),
    path('delete-category/<int:category_id>/', delete_category, name='deletecategory'),
    path('product/order/', CategoryOrderView.as_view(), name='module_order')

    # PRODUCT END
]
