# Create your views here.
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class EventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
        

