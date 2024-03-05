from rest_framework.decorators import api_view
from rest_framework.response import Response
from crudie.models import Crudie
from crudie.serializers import CrudieSerializer


@api_view(["POST", ])
def create(request):
    data = CrudieSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response(status=200, data=data.data)


@api_view(["GET", ])
def read(request):
    data = Crudie.objects.filter(service_key=request.GET.get("service_key")).first()
    serializer = CrudieSerializer(data)
    return Response(status=200, data=serializer.data)


@api_view(["PUT", ])
def update(request):
    data = Crudie.objects.filter(service_key=request.data.get("service_key")).first()
    data.data = request.data.get("data")
    data.save()
    serializer = CrudieSerializer(data)
    return Response(status=200, data=serializer.data)


@api_view(["DELETE", ])
def delete(request):
    data = Crudie.objects.filter(service_key=request.GET.get("service_key")).first()
    id = data.id
    serializer = CrudieSerializer(data)
    data.delete()
    return Response(status=200, data={**serializer.data, "id": id})
