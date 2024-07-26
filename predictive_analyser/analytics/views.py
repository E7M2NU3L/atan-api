from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_300_MULTIPLE_CHOICES

# 1. analyse
@api_view(['GET', 'POST'])
def analyse_customers(request):
    if request.method == "GET":
        context = {
            'data': request.data,
            'status': 200,
            'message': "The Analytics Data for customers has been feeded"
        }
        return Response(
            context,
            status=HTTP_200_OK
        )
    elif request.method == "POST":
        output = []
        context = {
            'status': 200,
            'message': "The Analytics has been done and the output is feeded",
            'output': output,
        }
        return Response(
            context,
            status=HTTP_200_OK
        )
    
# 2. stock analytics
@api_view(['GET', 'POST'])
def analyse_stock(request):
    if request.method == "GET":
        context = {
            'data': request.data,
            'status': 200,
            'message': "The Analytics Data for stock has been feeded"
        }
        return Response(
            context,
            status=HTTP_200_OK
        )
    elif request.method == "POST":
        output = []
        context = {
            'status': 200,
            'message': "The Analytics has been done and the output is feeded",
            'output': output,
        }
        return Response(
            context,
            status=HTTP_200_OK
        )