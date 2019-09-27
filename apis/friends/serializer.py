from apis.friends.models import Friends
from rest_framework import serializers



class FriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model =Friends 
        fields= ('pk','first_name','last_name','address','email','phone_no','gender','cover_image')


    def create(self,validate_data):

        friends = Friends(**validate_data)
        friends.save()
        return friends
        # news.author= self.request.user
       