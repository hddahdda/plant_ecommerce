from django.http import HttpResponse


class StripeWH_Handler:
    """ Required for stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a unexpected/generic or unknown webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a successfull payment_intent
        webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the peyment_intent.payment_failed webhook
        from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)