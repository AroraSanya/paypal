from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='index'),
    # path('paypal_return', views.paypal_return, name='paypal_return'),
    # path('paypal_cancel', views.paypal_cancel, name='paypal_cancel'),
    path('paypal', views.PaypalFormView.as_view(), name='paypal_cancel'),

  
]