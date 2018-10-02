from django.db import models
from django.conf import settings
#from django.contrib.auth import User
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

CONTRACT_STATUS = (
    ('OPPORTUNITY', 'Opportunity'),
    ('INITIAL', 'Initial'),
    ('PROCESSING', 'Processing'),
    ('CONFIRMED', 'Confirmed'),
    ('ACTIVE', 'Active'),
    ('CANCELED', 'Canceled'),
)

class PartnerType(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)

class Partner(models.Model):
    PartnerType = models.ForeignKey(PartnerType)
    OrganisationName = models.CharField(max_length=200)
    OrganisationDescription = models.CharField(max_length=800)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class AssetValueLifeCycle(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)
    DegradationPercentage = models.FloatField()
    IntervalInDays = models.IntegerField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class Contract(models.Model):
    OrganisationName = models.CharField(max_length=200)
    OrganisationDescription = models.CharField(max_length=800)
    TotalAmount = models.FloatField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class EntityAssetType(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class EntityAssetLocation(models.Model):
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)    
    NaturalStabilityRate = models.IntegerField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class EntityAsset(models.Model):
    Partner = models.ForeignKey(Partner)
    Contract = models.ForeignKey(Contract)
    EntityAssetType = models.ForeignKey(EntityAssetType)
    AssetValueLifeCycle = models.ForeignKey(AssetValueLifeCycle)    
    EntityAssetLocation = models.ForeignKey(EntityAssetLocation)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)    
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class InsuranceMetaType(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class InsuranceType(models.Model):
    InsuranceMetaType = models.ForeignKey(InsuranceMetaType)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800)   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class InsurancePolicy(models.Model):
    InsuranceType = models.ForeignKey(InsuranceType)
    IsTemplate = models.BooleanField()
    EffectiveDate = models.DateTimeField()
    ExpireDate = models.DateTimeField()
    Comment = models.CharField(max_length=800)  
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class PartnerMember(models.Model):
    Partner = models.ForeignKey(Partner)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class ContractDefinition(models.Model):    
    Contract = models.ForeignKey(Contract)
    PartnerMember = models.ForeignKey(PartnerMember)
    EntityAsset = models.ForeignKey(EntityAsset)
    InsurancePolicy = models.ForeignKey(InsurancePolicy)
    Description = models.CharField(max_length=800)
    Name = models.CharField(max_length=200)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class InsuranceTypeComplianceDocument(models.Model):
    InsuranceType = models.ForeignKey(InsuranceType)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800) 
    DocumentPath = models.CharField(max_length=800)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class ContractDefinitionUploadedDocument(models.Model):
    InsuranceTypeComplianceDocument = models.ForeignKey(InsuranceTypeComplianceDocument)
    ContractDefinition = models.ForeignKey(ContractDefinition)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=800) 
    DocumentPath = models.CharField(max_length=800)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class ContractStatus(models.Model):    
    Contract = models.ForeignKey(Contract)
    Status = models.CharField(max_length = 20, choices = CONTRACT_STATUS, default = 'INITIAL')
    Comment = models.CharField(max_length=800)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class InsurancePolicyAttribute(models.Model):
    InsurancePolicy = models.ForeignKey(InsurancePolicy)
    Description = models.CharField(max_length=800)
    Name = models.CharField(max_length=200)
    ExtraAmount = models.CharField(max_length=500)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class ContractExpense(models.Model):
    EntityAsset = models.ForeignKey(EntityAsset)
    Description = models.CharField(max_length=800)
    Amount = models.FloatField()   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)
    
class ContractExpenseDocument(models.Model):
    ContractExpense = models.ForeignKey(ContractExpense)
    DocumentPath = models.CharField(max_length=800)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(AUTH_USER_MODEL)
    DeletedBy = models.CharField(max_length=200)