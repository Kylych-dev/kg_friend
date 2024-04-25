from rest_framework import serializers
from utils.phone_normalize import normalize_phone_number
from django.contrib.auth.password_validation import validate_password
from apps.account.models import (
    CustomUser,
    # UserProfile,
    # ManagerProfile
)

class CustomUserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     write_only=True, required=True, validators=[validate_password]
    # )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField()
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        # if attrs.get('phone_number'):
        #     attrs['phone_number'] = normalize_phone_number(attrs['phone_number'])
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

# class UserSerializer(serializers.ModelSerializer):
#     user = CustomUserSerializer()
#
#     class Meta:
#         model = UserProfile
#         # fields = '__all__'
#         fields = [
#             # 'id',
#             'user'
#         ]
#
#     def create(self, validated_data):
#         print(validated_data, '-------- validate_data ----------')
#
#         user_data = validated_data.pop('user')
#         print(user_data, '------- user_data ------')
#         user_data.pop('password2')
#         role = user_data.pop('role')
#
#         user = CustomUser.objects.create_user(role=role, **user_data)
#         manager = UserProfile.objects.create(user=user, **validated_data)
#         return manager
#
#
# class ManagerSerializer(serializers.ModelSerializer):
#     user = CustomUserSerializer()
#
#     class Meta:
#         model = ManagerProfile
#         fields = '__all__'
#         # fields = [
#         #     # 'id',
#         #     'user'
#         #     'phone_number',
#         # ]
#
#     def create(self, validated_data):
#         print(validated_data, '-------- validate_data ----------')
#
#         user_data = validated_data.pop('user')
#         print(user_data, '------- user_data ------')
#         user_data.pop('password2')
#         role = user_data.pop('role')
#
#         user = CustomUser.objects.create_user(role=role, **user_data)
#         manager = ManagerProfile.objects.create(user=user, **validated_data)
#         return manager