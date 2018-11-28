from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from tasks.serializers import UserSerializer


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)


@api_view(["GET"])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET", "PUT"])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True})
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return Response({"message": "Deleted"})
