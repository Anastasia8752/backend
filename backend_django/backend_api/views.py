from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializer import QuestionSerializer


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)