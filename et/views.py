from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.serializers import serialize
from rest_framework import status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

from models import PartnerType
from models import PartnerMember
from models import Partner
from models import Contract
from models import ContractDefinition
from models import EntityAsset
from models import EntityAssetType
from models import EntityAssetLocation
from models import InsuranceMetaType
from models import InsurancePolicy
from models import InsurancePolicyAttribute
from models import InsuranceType

from django.forms import ModelForm

def home(request):
    return render(request, 'index.html')

# Account context definition models
#def signup(request):
#    return render(request, 'signup.html')

# Partner context definition models
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def newpartner(request):
    partner = PartnerType()
    partner = request.data['PartnerType']
    partner.Name = request.data['Name']
    partner.Description = request.data['Description']
    partner.Author = request.user
    partner.save()
    return JsonResponse(request)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def partner(request, id):
    return JsonResponse(Partner.objects.get(id = id))

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partners(request):
    return JsonResponse(list(Partner.objects.values()), safe=False)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def newpartnertype(request):
    partnerType = PartnerType()
    partnerType.Name = request.data['Name']
    partnerType.Description = request.data['Description']
    partnerType.Author = request.user
    partnerType.save()
    return JsonResponse('Partner type added', safe=False)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partnertype(request, id):
    return JsonResponse(model_to_dict(PartnerType.objects.get(id = id)), safe=False)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partnertypes(request):
    return JsonResponse(list(PartnerType.objects.values()), safe=False)

# EntityAsset context definition models
def entityassettype(request):
    return JsonResponse('EntityAssetType', safe=False)

# Insurance context definition models
def insurancetype(request):
    return JsonResponse('InsuranceType', safe=False)

# Contract context definition models



# ModelForms
# class PartnerTypeForm(ModelForm):
#      class Meta:
#          model = PartnerType
#          fields = ['Name', 'Description']
# 
# class PartnerForm(ModelForm):
#      class Meta:
#          model = Partner
#          fields = ['PartnerType', 'OrganisationName', 'OrganisationDescription']


# Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password")

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.data['email'],
            serialized.data['username'],
            serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


