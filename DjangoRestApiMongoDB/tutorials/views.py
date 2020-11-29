from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.db.models import Q 


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials

    if request.method == 'GET':
        tutorials = Tutorial.objects.all().order_by('firstname')
        
        query = request.GET.get('q', None)
        if query is not None:
            tutorials  = tutorials.filter(
                Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(gender__icontains=query) | Q(phoneno__icontains=query)
            )
        # firstname = request.GET.get('q')

        # if firstname is not None:
        #     tutorials = tutorials.filter(firstname__icontains=firstname)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Contacts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The contact does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
    
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Contact was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
    # GET / PUT / DELETE tutorial
    
        
# @api_view(['GET'])
# def tutorial_list_published(request):
#     # GET all published tutorials

#     tutorials = Tutorial.objects.filter(Mobile_Phone=Mobile_Phone)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)