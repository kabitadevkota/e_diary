from apis.meetings.models import Meetings
from rest_framework import serializers



class MeetingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meetings 
        fields= ('pk','title','date','time','venue','status')

    def create(self,validate_data):

        meetings = Meetings(**validate_data)
        meetings.save()
        return meetings