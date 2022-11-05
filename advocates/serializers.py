from rest_framework.serializers import ModelSerializer
from .models import Company, Advocates

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AdvocatesSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocates
        fields = ['profile_pic', 'username', 'name', 'bio', 'company', 'twitter']

