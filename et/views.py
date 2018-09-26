from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

def home(request):
    return render(request, 'index.html')

# Account context definition models
def signup(request):
    return render(request, 'signup.html')

# Partner context definition models
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def partnertype(request):
    partnerType = PartnerType()
    #partnerType.Name = request["Name"]
    #partnerType.Description = "PType1 description 123"
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