#urls.py
from django.conf.urls import *
from django.views.generic.base import RedirectView

import stripe

urlpatterns = patterns('sample_stripe.views', 
    url(r'^stripe_test/$', 'stripe_test', name='stripe_test'),
)