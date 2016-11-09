from rest_framework import serializers
from django.contrib.auth.models import User


class DynamicFieldsSerializer(object):
    """
    serializer = UserSerializer(fields=['your', 'fields', 'here'])

    -- or --

    serializer = UserSerializer(remove_fields=['field', 'to', 'remove'])
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        remove_fields = kwargs.pop('remove_fields', None)
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)

        if fields:
            [self.fields.pop(field) for field in self.fields if
             field not in fields]

        if remove_fields:
            [self.fields.pop(field) for field in self.fields if
             field in remove_fields]


class UserSerilizer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'groups')
