from rest_framework import serializers
from .models import Question, Answer
from django.contrib.auth.models import User
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()



class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = serializers.CharField()
    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        answers = obj.answer.all()
        ser_answers = AnswerSerializer(instance=answers, many=True)
        return ser_answers.data



class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model = Answer
        fields = "__all__"




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"