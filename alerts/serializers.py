from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["message", "timestamp", "user", "asset_id", "min_value", "max_value"]
