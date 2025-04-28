from users.models import Users
from documents.models import Document
from signatures.models import Signatures

from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
            


        
class SignatureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested serializer
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), source='user', write_only=True)

    class Meta:
        model = Signatures
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested serializer
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), source='user', write_only=True)

    class Meta:
        model = Document
        fields = '__all__'