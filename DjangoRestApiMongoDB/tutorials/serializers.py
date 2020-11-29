from rest_framework import serializers 
from tutorials.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = (
          'id',
          'firstname',
          'lastname',
          'gender',
          'emailid',
          'phoneno',
        )