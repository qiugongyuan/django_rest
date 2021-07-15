from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Event, Guest


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# serializers用于定义api的表现形式，如返回了哪些字段，返回了怎样的格式。这里序列化django自带的user和Group
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'name', 'address', 'start_time', 'limit','status')


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('url', 'realname', 'phone', 'email', 'sign', 'event')
