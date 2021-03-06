"""HTTP endpoints for interacting with payments."""
from __future__ import absolute_import

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.cache.decorators import cache_response

from ecommerce.extensions.api import serializers

PAYMENT_PROCESSOR_CACHE_KEY = 'PAYMENT_PROCESSOR_LIST'
PAYMENT_PROCESSOR_CACHE_TIMEOUT = 60 * 30


class PaymentProcessorListView(generics.ListAPIView):
    """List the available payment processors

    Note:
        This endpoint is *deprecated*. There is no use case for this given that the payment page
        is served by this service (rather than LMS), and the new page loads payment processors
        via server-side rendering (rather than client-side).
    """
    pagination_class = None
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PaymentProcessorSerializer

    @cache_response(
        PAYMENT_PROCESSOR_CACHE_TIMEOUT,
        key_func=lambda *args, **kwargs: PAYMENT_PROCESSOR_CACHE_KEY,
        cache_errors=False,
    )
    def get(self, request, *args, **kwargs):
        return super(PaymentProcessorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        """Fetch the list of payment processor classes based on Django settings."""
        return self.request.site.siteconfiguration.get_payment_processors()
