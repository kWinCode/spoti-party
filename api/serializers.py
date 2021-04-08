from rest_framework import serializers
from .models import Room

# for response
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

# data for post request has to fit:
class CreateRoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class UpdateRoomSerializer (serializers.ModelSerializer):
    # modify code, because otherwise will throw error as code in models is defined as unique
    code = serializers.CharField(validators=[])
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')