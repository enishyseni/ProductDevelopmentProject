from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    model = PartnerForm(request.POST);
    return JsonResponse(request)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def partner(request, id):
    return JsonResponse(Partner.objects.get(id = id))

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partners(request):
    partner = Partner()
    return JsonResponse(Partner.objects.get())

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def newpartnertype(request):
    #partnerType = PartnerType()
    return JsonResponse(request)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partnertype(request):
    partnerType = PartnerType()
    return JsonResponse('PartnerType')

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partnertypes(request):
    return JsonResponse(PartnerType.objects.get())

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partners(request):
    return JsonResponse(Partner.objects.get())

# EntityAsset context definition models
def entityassettype(request):
    return JsonResponse('EntityAssetType')

# Insurance context definition models
def insurancetype(request):
    return JsonResponse('InsuranceType')

# Contract context definition models



# ModelForms

class PartnerForm(ModelForm):
     class Meta:
         model = Partner
         fields = ['PartnerType', 'OrganisationName', 'OrganisationDescription']


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


