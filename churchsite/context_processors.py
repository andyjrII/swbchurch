from django.conf import settings


def paystack_key(request):
    """Make Paystack public key available in all templates"""
    return {
        'PAYSTACK_PUBLIC_KEY': settings.PAYSTACK_PUBLIC_KEY,
    }
