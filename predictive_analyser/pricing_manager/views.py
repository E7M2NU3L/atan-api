from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_300_MULTIPLE_CHOICES, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.generics import RetrieveAPIView, CreateAPIView, RetrieveDestroyAPIView, ListAPIView
from pricing_manager import models
from pricing_manager import serializers

# 1. List payment view
class ListPayments(ListAPIView):
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializers.PaymentSerializer

    def list(self, request):
        query_set = self.get_queryset()
        serializer = serializers.PaymentSerializer(query_set, many = True)
        
        context = {
            "status": 200,
            "message": "the payment Data",
            "data": serializer.data
        }
        return Response(
            context, status=HTTP_200_OK
        )

# 2. Create Payment view    
class CreatePayment(CreateAPIView):
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializers.PaymentSerializer

# 3. Cancel Payment view
class CancelPayment(RetrieveDestroyAPIView):
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializers.PaymentSerializer

# 4. Get Single Payment Info
class SinglePayment(RetrieveAPIView):
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializers.PaymentSerializer
