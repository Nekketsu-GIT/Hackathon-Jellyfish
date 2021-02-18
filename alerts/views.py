from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from alerts.models import Alert
from .serializers import AlertSerializer


class AlertListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        alerts = Alert.objects.filter(user=request.user.id)
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'message': request.data.get('message'),
            'timestamp': request.data.get('timestamp'),
            'user': request.user.id,
            'asset_id': request.data.get('asset_id'),
            'max_value': request.data.get('max_value'),
            'min_value': request.data.get('min_value')
        }
        serializer = AlertSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlertDetailApiView(APIView):

    def get_object(self, alert_id):
        try:
            return Alert.objects.get(id=alert_id)
        except Alert.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, alert_id, *args, **kwargs):
        alert_instance = self.get_object(alert_id)
        if not alert_instance:
            return Response(
                {"res": "Alert with alert id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AlertSerializer(alert_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, alert_id, *args, **kwargs):
        alert_instance = self.get_object(alert_id)
        if not alert_instance:
            return Response(
                {"res": "Alert with alert id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'message': request.data.get('message'),
            'timestamp': request.data.get('timestamp'),
            'user': request.user.id,
            'asset_id': request.data.get('asset_id'),
            'max_value': request.data.get('max_value'),
            'min_value': request.data.get('min_value')
        }
        serializer = AlertSerializer(instance=alert_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, alert_id, *args, **kwargs):
        alert_instance = self.get_object(alert_id)
        if not alert_instance:
            return Response(
                {"res": "Alert with alert id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        alert_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


def get_alerts(request):
    alerts = Alert.objects.filter(user=request.user.id)
    context = {'alerts_list': alerts}
    return render(request, 'alertes/alertes.html', context)


def add_alert(request):
    if request.method == 'POST':
        Alert.objects.create(
            message=request.POST.get('message'),
            user_id=request.user.id,
            asset_id=request.POST.get('asset_id'),
            min_value=request.POST.get('min_value'),
            max_value=request.POST.get('max_value')

        )

    return render(request, 'alertes/single_alerte.html')


"""
api = CoinAPIv1(api_key)


assets = api.metadata_list_assets()
priceBtc = assets[0]['price_usd']
print(priceBtc)
if priceBtc < 5000:
    Alert.objects.create(message='Under 5000')
    send_mail('Under 5000', 'BTC falls under 5000', EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)
elif priceBtc > 7000:
    Alert.objects.create(
        message='Above 7000'
    )
    send_mail('Above 7000', 'BTC is above 7000', EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)
else:
    print("No Alert")


"""

"""
for asset in assets:
    if asset['asset_id'] == 'BTC':
        priceBtc = asset['price_usd']
        if priceBtc < 5000:
            subject = 'Under 5000'
            message = 'BTC falls under 5000'
            Alert.objects.create(message=subject)
            send_mail(subject, message, EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)
        elif priceBtc > 7000:
            subject = 'Above 7000'
            message = 'BTC is above 7000'
            Alert.objects.create(
                message=subject
            )
            send_mail(subject, message, EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)

        else:
            print("No Alert")
        break
        
"""

"""
# real time data using webSocket api
from websocket import create_connection
import json

ws = create_connection("wss://ws.coinapi.io/v1")
sub = CoinAPIv1_subscribe(api_key)
ws.send(json.dumps(sub.__dict__))
while True:
    resp = ws.recv()
    msg = json.loads(resp)
    if float(msg['price']) < 5000:
        subject = 'Under 5000'
        message = 'BTC falls under 5000'
        Alert.objects.create(
            message=subject
        )
    if float(msg['price']) > 7000:
        subject = 'Above 7000'
        message = 'BTC is above 7000'
        Alert.objects.create(
            message=subject
        )

    send_mail(subject, message, EMAIL_HOST_USER, ['josedacosta339@gmail.com'], fail_silently=False)

ws.close()

"""
