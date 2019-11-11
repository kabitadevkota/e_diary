from apis.notes.models import Notes
from rest_framework import serializers



class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes 
        fields= ('pk','title','created_date','description','status')


    def create(self,validate_data):

        notes = Notes(**validate_data)
        notes.save()
        return notes
