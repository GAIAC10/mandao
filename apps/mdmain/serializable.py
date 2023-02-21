from rest_framework import serializers


from apps.mdauth.serializable import UserSerializer
from apps.mdmain.models import CommentNews


class CommentSerizlizer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = CommentNews
        fields = ('id','content','author','pub_time')