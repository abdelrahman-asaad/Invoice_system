from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    #custom field to be serialized
    #write_only = True means that password is sending in request only
    #but not in viewed in response

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        #fields to be serialized
        

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'sales')
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Serializer مخصص لتحديث الدور فقط
class UpdateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["role"]  # بس الدور هو اللي يتعدل

    def validate_role(self, value): #custom validation instead of built-in validation to add custom response msg 
        valid_roles = [choice[0] for choice in User.ROLE_CHOICES]
        if value not in valid_roles:
            raise serializers.ValidationError(
                f"Invalid role. Allowed roles are: {', '.join(valid_roles)}"
            )
        return value