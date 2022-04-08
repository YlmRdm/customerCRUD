from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('', views.readCustomer),
    path('create', views.createCustomer),
    path('edit/<int:id>', views.editCustomer),
    path('update/<int:id>', views.updateCustomer),
    path('delete/<int:id>', views.destroyCustomer),
    path('admin/', admin.site.urls),
]
