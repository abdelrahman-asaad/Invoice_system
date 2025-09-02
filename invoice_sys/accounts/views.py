from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer, UpdateRoleSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwner, IsOwnerOrManager

User = get_user_model()


# Register new user
class RegisterView(generics.CreateAPIView):  # CreateAPIView >> POST
    queryset = User.objects.all() 
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # أي حد يقدر يعمل Register


# List users (Owner فقط أو Owner + Manager على حسب متطلباتك)
class UserListView(generics.ListAPIView):  # ListAPIView >> GET
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrManager]  # Owner أو Manager هما اللي يقدروا يشوفوا المستخدمين



class UpdateUserRoleView(generics.UpdateAPIView): #to allow owner to set roles to users
    queryset = User.objects.all()
    serializer_class = UpdateRoleSerializer
    permission_classes = [IsOwner]