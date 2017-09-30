import json

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


import stripe  

# Create your views here.
class StripeTest(View):
    template_name = "stripe/stripe_payment.html"

    def get(self, request, *args, **kwargs):
        data=[]
        publishable = "pk_test_G9jwZAv7Y6z7nC5MHCNnvxGN"

        sdata = {
            'publishable': publishable
        }
        return render(request, self.template_name, sdata)

    def post(self, request, *args, **kwargs):
        data = {}
        stripe.api_key = "sk_test_vvFNpPr85Zz32hY649qf22bB"
        token = request.POST.get('stripeToken')
        case_id = request.POST.get('caseId') 
        amount_charge = request.POST.get('amount') 
        amount_charged=int(amount_charge)*100
        try:
           charge = stripe.Charge.create(
                amount=amount_charged,
                currency="usd",
                description="Stripe Sample Fee",
                source=token)
           print charge,"charge"
        except:
            pass

        return HttpResponseRedirect(reverse('stripe_test'))


stripe_test = StripeTest.as_view()