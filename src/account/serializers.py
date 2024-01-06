from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["is_staff"] = self.user.is_staff
        attrs["is_superuser"] = self.user.is_superuser
        attrs["is_active"] = self.user.is_active
        attrs["full_name"] = self.user.first_name + " " + self.user.last_name
        attrs["email"] = self.user.email
        # attrs["organization"] = self.user.organization.shortname if self.user.organization else None
        # attrs["organization_id"] = self.user.organization.id if self.user.organization else None
        # attrs["state_id"] = self.user.state.id if self.user.state else None
        # attrs["language"] = self.user.language.name if self.user.language else None
        # attrs["language_id"] = self.user.language.id if self.user.language else None
        attrs["groups"] = [group.name for group in self.user.groups.all()]
        attrs["permissions"] = [permission.name for permission in self.user.user_permissions.all()]
        return attrs


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
