from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_300_MULTIPLE_CHOICES, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.decorators import api_view

# 1. collect data
@api_view(['GET'])
def receive_feedbacks(request):
    context = {
        'data': request.data,
        'status': 200,
        'message': "Feedback has been received"
    }
    return Response(context, status=200)

# 2. Create custom Form
@api_view(['POST'])
def send_forms(request):
    context = {
        'status': 200,
        'message': "Feedback has been received"
    }
    return Response(context, status=200)