from rest_framework.serializers import ModelSerializer
from .models import Task
from rest_framework import serializers
class TaskSerializer(ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id','user', 'title','absolute_url', 'complete', 'created_date', 'updated_date']     
        
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)  
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url', None)
        
        return rep     
    
    
