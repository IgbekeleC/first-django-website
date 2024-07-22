from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    
    #path('gallery/', views.gallery, name='gallery'),
    path('product/', views.product, name='gallery-products'),
    path('product/new', views.product_add, name='product_add'),
    
    path('product/delete/<int:pk>/', views.product_delete,
         name='gallery-products-delete'),
    path('product/<int:pk>/', views.product_detail,
         name='product-detail'),
    #path('product/detail/<int:pk>/', views.product_detail, name='product-detail'),
    path('product/edit/<int:pk>/', views.product_edit,
         name='gallery-product-edit'),
    path('customer/', views.customer, name='customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='customer-detail'),
    path('order/', views.order, name='order'),
    path('customer/', views.customer, name='customer'),
    path('customer/detial/<int:pk>/', views.customer_detail,
         name='customer-detail'),
    path('project/', views.project, name = 'project'),
    path('account/', views.account, name = 'account'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)