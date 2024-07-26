from rest_framework.serializers import ModelSerializer
from pricing_manager import models

class PaymentSerializer(ModelSerializer):
    class meta:
        model = models.PaymentModel
        fields = "__all__"