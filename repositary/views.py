from django.shortcuts import render
from repositary.models import Questions
from repositary.serializer import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class QuestionListCreateView(APIView):

    def get(self,request):
        qs=Questions.objects.all()  #colection of questions
        serializer_instance=QuestionSerializer(qs,many=True)  #many=true means tells the serializer that the input contains multiple objects
        return Response(serializer_instance.data) #return the serializer data as a response
    
    def post(self,request):
        form_data=request.data #form_data dictionary to python native type
        serializer_instance=QuestionSerializer(data=form_data)#create serializer instance with form data
        if serializer_instance.is_valid():#check if the data is valid according to the serializers validation rule
            actual_data=serializer_instance.validated_data#Get the validation data from  the serializer
            Questions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

class QuestionRetriveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = Questions.objects.get(id=pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            Questions.objects.filter(id=pk).update(**actual_data)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
    