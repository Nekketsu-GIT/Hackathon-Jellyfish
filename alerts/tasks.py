from coinapi_rest_v1.restapi import CoinAPIv1
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.core.mail import send_mail

from alerts.CoinAPIv1_Service import api_key
from alerts.models import Alert


def notify_user_btc():
    api = CoinAPIv1(api_key)
    alerts = Alert.objects.all()
    assets = api.metadata_list_assets()
    if alerts:
        for alert in alerts:
            for asset in assets:
                if asset['asset_id'] == alert.asset_id:
                    priceBtc = asset['price_usd']
                    print(priceBtc)
                    if priceBtc < alert.min_value:
                        send_mail('Under 5000', 'BTC falls under 5000', EMAIL_HOST_USER, [User.objects.get(id = alert.user_id).email],
                                  fail_silently=False)
                    elif priceBtc > alert.max_value:
                        send_mail('Above 7000', 'BTC is above 7000', EMAIL_HOST_USER, [User.objects.get(id = alert.user_id).email],
                                  fail_silently=False)
                    else:
                        print("No Alert sended")
    else:
        print("No Alert defined")
"""
    priceBtc = assets[0]['price_usd']
    print(priceBtc)
    if priceBtc < 5000:
        Alert.objects.create(message='Under 5000')
        send_mail('Under 5000', 'BTC falls under 5000', EMAIL_HOST_USER, ['josedacosta339@gmail.com'],
                  fail_silently=False)
    elif priceBtc > 7000:
        Alert.objects.create(
            message='Above 7000'
        )
        send_mail('Above 7000', 'BTC is above 7000', EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)
    else:
        print("No Alert")
"""