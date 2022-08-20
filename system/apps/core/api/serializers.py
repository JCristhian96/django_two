from rest_framework import serializers
# Models
from apps.core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__' 
        
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url)