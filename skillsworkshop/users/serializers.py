from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# create code below


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    bio = serializers.CharField()
    phone_number = serializers.CharField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    location = serializers.CharField(max_length=200)
    profile_picture = serializers.URLField()
    is_mentor = serializers.BooleanField()
    is_mentee = serializers.BooleanField(default=True)
    is_private = serializers.BooleanField(default=False)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'bio', 'phone_number', 'first_name', 'last_name',
                  'email', 'location', 'profile_picture', 'password', 'password2', 'is_mentor', 'is_mentee', 'is_private', 'id']
        read_only_fields = ['id', 'is_private', 'is_mentee']
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Your password fields didn't match."})
        return attrs


class CustomUserDetailSerializer(CustomUserSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'password2']
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get
        ('first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.password2 = validated_data.get('datetime', instance.password2)
        instance.save()
        return instance


class CustomUserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Your password fields didn't match."})

        return attrs
