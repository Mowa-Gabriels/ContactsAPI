from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Contact


class ContactSerializer(HyperlinkedModelSerializer):


    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # country_code = models.CharField(max_length=3)
    # first_name =  models.CharField(max_length=30)
    # last_name =  models.CharField(max_length=30)
    # phone_number =  models.CharField(max_length=30)
    # contact_picture = models.URLField(null=True)
    # is_favorite = models.BooleanField(default=False)
    owner = serializers.ReadOnlyField(source='owner.last_name')
    url = serializers.HyperlinkedIdentityField(view_name='contact-detail', format='html')

    
    class Meta:

        model = Contact
        fields = '__all__'