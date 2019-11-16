from apis.friend.models import Friend
from rest_framework import serializers



class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model =Friend 
        fields= ('pk','first_name','last_name','address','email','phone_no','gender','cover_image')


    def create(self,validate_data):

        friend = Friend(**validate_data)
        friend.save()
        return friend
        # news.author= self.request.user
       