from rest_framework import generics


from api.users.models import User, UserSerializer


class Users(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
