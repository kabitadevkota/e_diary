from rest_framework import serializers
from apis.accounts.models import Users




class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Users
        fields = ['pk','email', 'password', 'address','first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        raw_password = validated_data.pop('password')
        users =Users(**validated_data)
        users.set_password(raw_password)
        users.save(users)

        users.objects.create(**profile_data)
        return users


class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['pk', 'first_name', 'last_name', 'username','password', 'email','address']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        # profile_instance = instance.Users
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.address = validated_data.get("address", instance.address)
        instance.user_picture = validated_data.get("user_picture", instance.user_picture)

        if validated_data.get("password"):
            instance.set_password(validated_data.get("password"))

        return instance 