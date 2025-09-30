from rest_framework.decorators import api_view
from rest_framework.response import Response
from crudie.models import FooBar
from crudie.serializers import FooBarSerializer

@api_view(["GET",])
def healthcheck(request):
    return Response(status=200)

@api_view(["POST", ])
def create(request):
    data = FooBarSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response(status=200, data=data.data)
    return Response(status=400)


@api_view(["GET", ])
def read(request, id):
    foobar = FooBar.objects.filter(id=id).first()
    serializer = FooBarSerializer(foobar)
    return Response(status=200, data=serializer.data)


@api_view(["PUT", "PATCH"])
def update(request, id):
    foobar = FooBar.objects.filter(id=id).first()
    foobar.foo = request.data.get("foo") or foobar.foo
    foobar.bar = request.data.get("bar") or foobar.bar
    foobar.save()
    serializer = FooBarSerializer(foobar)
    return Response(status=200, data=serializer.data)


@api_view(["DELETE", ])
def delete(request, id):
    foobar = FooBar.objects.filter(id=id).first()
    serializer = FooBarSerializer(foobar)
    foobar.delete()
    return Response(status=200, data=serializer.data)
