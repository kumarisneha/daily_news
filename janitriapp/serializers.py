from django.core import serializers
from django.contrib.auth.models import User
from janitriapp.models import UserInterest, NewsWebsite


json_serializer = serializers.get_serializer("json")()