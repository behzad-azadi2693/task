from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NameSerializer, CellSerializer, RoadSerializer, HouseNumberSerializer
from django.http import JsonResponse


@api_view(['GET','POST'])
def check_field(request, field):
    
        if request.method == 'POST':
            if field == 'name':
                srz = NameSerializer(data = request.data)
                if srz.is_valid():
                    return JsonResponse({"msg":"مقدار صحیح است"}, status=200)
                else:
                    return JsonResponse({"data":srz.errors}, status=400)

            if field == 'cell':
                srz = CellSerializer(data = request.data)
                if srz.is_valid():
                    return JsonResponse({"msg":"مقدار صحیح است"}, status=200)
                else:
                    return JsonResponse({"data":srz.errors}, status=400)
            
            if field == 'road':
                srz = RoadSerializer(data = request.data)
                if srz.is_valid():
                    return JsonResponse({"msg":"مقدار صحیح است"}, status=200)
                else:
                    return JsonResponse({"data":srz.errors}, status=400)

            if field == 'house_number':
                srz = HouseNumberSerializer(data = request.data)
                if srz.is_valid():
                    return JsonResponse({"msg":"مقدار صحیح است"}, status=200)
                else:
                    return JsonResponse({"data":srz.errors}, status=400)