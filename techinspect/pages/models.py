from pages import db_validators as dbv

from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models 

from django.db.models import *


class TIUser(AbstractUser): 
    VIN = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=True) #Have to link by name of class since it is created later on in file
    waiverID = models.ForeignKey('Waiver', on_delete=models.CASCADE, null=True) #same here
    image = models.ImageField(upload_to='images', null=True)
    def __str__(self):
        return self.username + " " + self.password #TODO remove this after project complete

class Vehicle(models.Model): 
    VIN = models.CharField(max_length=17, primary_key=True) 
    vehicleYear = models.IntegerField(validators=[dbv.validate_car_year])
    vehicleMake = models.CharField(max_length=50) 
    vehicleModel = models.CharField(max_length=50) 
    inspectionID = models.ForeignKey('Inspection', on_delete=models.CASCADE, null=True) #deleting a car deletes its inspection 
    vehicleAvatar = models.ImageField(upload_to='images', null=True)
    UUID = models.ForeignKey(TIUser, on_delete=models.DO_NOTHING) #Is this correct?
    def __str__(self):
        return f"Vehicle info: {self.VIN}, {self.UUID}"
    


class Inspection(models.Model): 
    #TODO: Is defining an ID here necessary or should we just use the one provided by Django?

    UserVehicle = models.ForeignKey(Vehicle, on_delete=DO_NOTHING) #Shouldn't delete a car when the inspection is deleted

    inspectionID = models.AutoField(primary_key=True) 
    inspectionDate = models.DateField(default=date.today) 
    #Exterior checks
    noWheelPlay = models.BooleanField(default=False)
    goodWheels = models.BooleanField(default=False)
    goodHubCaps = models.BooleanField(default=False)
    goodTires = models.BooleanField(default=False)
    goodTireTreadDepth = models.BooleanField(default=False)
    goodBreakPads = models.BooleanField(default=False)
    noLooseBodyPanels = models.BooleanField(default=False)
    goodNumbers = models.BooleanField(default=False)

    #Interior checks
    goodFloorMats = models.BooleanField(default=False)
    secureBTC = models.BooleanField(default=False)
    goodBreakPedal = models.BooleanField(default=False)
    noExcessPlayinSteering = models.BooleanField(default=False)
    goodSeat = models.BooleanField(default=False)
    goodSeatBelt = models.BooleanField(default=False)
    goodMountedCamera = models.BooleanField(default=False)

    #Under the Hood and Trunk
    goodBatteryandConnections = models.BooleanField(default=False)
    goodBatteryandConnectionsNotes = models.CharField(max_length=100, default="") 
    goodAirIntakeandSecure = models.BooleanField(default=False)
    goodAirIntakeandSecureNotes = models.CharField(max_length=100, default="") 
    goodThrottleCable = models.BooleanField(default=False)
    goodThrottleCableNotes = models.CharField(max_length=100, default="") 
    goodFluidCaps = models.BooleanField(default=False)
    goodFluidCapsNotes = models.CharField(max_length=100, default="") 
    noMajorLeaks = models.BooleanField(default=False)
    noMajorLeaksNotes = models.CharField(max_length=100, default="") 
    emptyTrunk = models.BooleanField(default=False)
    emptyTrunkNotes = models.CharField(max_length=100, default="") 
    functionalExhaust = models.BooleanField(default=False)
    functionalExhaustNotes = models.CharField(max_length=100, default="") 
     
    #helmet
    goodHelmet = models.BooleanField(default=False)
    
    #Novice driver
    isNoviceDriver = models.BooleanField(default=False)
    Verified = models.BooleanField(default=False) #Only verified if an admin approves it/does the inspection 

class Waiver(models.Model): 
    #TODO: Is defining an ID here necessary or should we just use the one provided by Django?
    waiverID = models.AutoField(primary_key=True) 
    waiverDate = models.DateField(default=date.today) 
    waiverName = models.CharField(max_length=100) 
    UUID = models.ForeignKey(TIUser, on_delete=DO_NOTHING) 

class Image(models.Model):
    #TODO: Is defining an ID here necessary or should we just use the one provided by Django?
    imageID = models.AutoField(primary_key=True) 
    waiverID = models.ForeignKey(Waiver, on_delete=models.CASCADE, null=True) #Deleting an inspection deletes the photo, 
                                                                              #because we include and imageID in TIUser we can't force a waiver FK
    image = models.ImageField(upload_to='images', null=True)











