from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.manager_login, name='manager_login'),
     path('manager_signup/', views.manager_signup, name='manager_signup'),
     path('manager_dashboard', views.manager_dashboard, name='manager_dashboard'),
     path('list_product',views.list_product,name = 'list_product'),
     path('create_product',views.create_product,name='create_product'),
     path('update_product/<int:pk>/',views.update_product,name='update_product'),
     path('delete_product/<int:pk>/',views.delete_product,name='delete_product'),
     path('book_appointment',views.book_appointment, name='book_appointment'),
     path('list_services',views.list_services,name ='list_services'),
     path('create_service',views.create_service, name='create_service'),
     path('update_service/<int:pk>/',views.update_service,name='update_service'),
     path('delete_service/<int:pk>/',views.delete_service,name='delete_service'),
     path('create_appointment', views.create_appointment,name="create_appointment"),
     path('display_bill',views.display_bill, name='display_bill'),
     path('booked_appointment',views.booked_appointment, name='booked_appointment'),
     path('create_package',views.create_package,name='create_package'),
     path('list_package',views.list_package,name= 'list_package'),
     path('update_package/<int:pk>/', views.update_package, name='update_package'),
     path('delete_package/<int:pk>/',views.delete_package,name='delete_package'),
     path('list_cutomer',views.list_customer,name='list_customer'),
     path('create_customer',views.create_customer,name='create_customer'),
     path('update_customer/<int:pk>',views.update_customer,name='update_customer'),
     path('delete_customer/<int:pk>',views.delete_customer,name='delete_customer'),
     

     
    
     
     ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)