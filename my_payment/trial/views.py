# from django.shortcuts import render,redirect
# from django.urls import reverse
# from django.conf import settings
# from django.contrib import messages
# import uuid
# from paypal.standard.forms import PayPalPaymentsForm
# # Create your views here.

# def home(request):
#     host=request.get_host()
#     paypal_dict = {
#         'buisness':settings.PAYPAL_RECEIVER_EMAIL,
#         'amount':'20.00',
#         'item_name':'Product',
#         'currency_code': 'USD',
#         'invoice':str(uuid.uuid4()),
#         'notify_url': f'http://{host}{reverse("paypal-ipn")}',
#         'return_url': f'http://{host}{reverse("paypal_return")}',
#         'cancel_return': f'http://{host}{reverse("paypal_cancel")}',
#     }
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context={'form':form}
#     return render(request,'payment.html' ,context)

# def paypal_return(request):
#     messages.success(request,'got sucess')
#     return redirect('home')

# def paypal_cancel(request):
#     messages.success(request,'got cancelled')
#     return redirect('home')





# # from django.shortcuts import render
 

# # def index(request):
# #     return render(request, 'payment.html')
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from paypal.standard.forms import PayPalPaymentsForm

from rest_framework.views import APIView
from rest_framework.response import Response
from paypal.standard.forms import PayPalPaymentsForm

class PaypalFormView(APIView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get(self, request, format=None):
        initial_data = {
            'business': 'your-paypal-business-address@example.com',
            'amount': 20,
            'currency_code': 'EUR',
            'item_name': 'Example item',
            'invoice': 1234,
            'lc': 'EN',
            'no_shipping': '1',
        }
        form = self.form_class(initial=initial_data)
        return Response({'form': form.render()}, template_name=self.template_name)

    def post(self, request, format=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process the form data or save to database
            # You can access form fields using form.cleaned_data

            # Return a success response
            return Response({'success': True})
        else:
            # Return a failure response with form errors
            return Response({'success': False, 'errors': form.errors})
