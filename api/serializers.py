from rest_framework import serializers
from api.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name' ,'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password = serializers.CharField(write_only=True)



from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

