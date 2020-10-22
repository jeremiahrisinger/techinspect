from django.db import models 

from django.db.models import *
  

# Create your models here. 
class Image(models.Model):
    imageID = models.CharField(max_length=34, primary_key=True)

class User(models.Model): 
    UUID = models.CharField(max_length=34, primary_key=True)
    firstName = models.CharField(max_length=30) 
    middleInitial = models.CharField(max_length=1) 
    lastName = models.CharField(max_length=50) 
    VIN = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=False) #Have to link by name of class since it is created later on in file
    waiverID = models.ForeignKey('Waiver', on_delete=models.CASCADE, null=False) #same here
    imageID = models.ForeignKey('Image', on_delete=models.CASCADE, null=False) #and here
    def login(self, email, enc_pswd):
        #try:
        #    user = User.objects.filter(pk=email)
        pass

class Vehicle(models.Model): 
    VIN = models.CharField(max_length=17, primary_key=True) 
    vehicleYear = models.IntegerField() #TODO: include a validator here for ensuring the age of the car isn't malformed.
    vehicleMake = models.CharField(max_length=50) 
    vehicleModel = models.CharField(max_length=50) 
    inspectionID = models.ForeignKey('Inspection', on_delete=models.CASCADE, null=False) #deleting a car deletes its inspection 
    UUID = models.ForeignKey(User, on_delete=models.DO_NOTHING) #Is this correct?


class Inspection(models.Model): 
    inspectionID = models.CharField(max_length=34, primary_key=True) 
    inspectionDate = models.CharField(max_length=30) 
    exteriorInspection = models.CharField(max_length=100) 
    interiorInspection = models.CharField(max_length=100) 
    hoodTrunkInspection = models.CharField(max_length=100) 
    helmetInpsection = models.CharField(max_length=100) 
    ExteriorApproval = models.BooleanField(default=False)#TODO add 
    InteriorApproval = models.BooleanField(default=False) 
    HoodApproval = models.BooleanField(default=False) 
    TrunkApproval = models.BooleanField(default=False) 
    Other = models.CharField(max_length = 140) 
    Verified = models.BooleanField(default=False) #Only verified if an admin approves it/does the inspection 
    VIN = models.ForeignKey(Vehicle, on_delete=DO_NOTHING) #Shouldn't delete a car when the inspection is deleted

class Waiver(models.Model): 
    waiverID = models.CharField(max_length=34, primary_key=True) 
    waiverDate = models.CharField(max_length=30) 
    waiverComplete = models.CharField(max_length=100) 
    UUID = models.ForeignKey(User, on_delete=DO_NOTHING) 

