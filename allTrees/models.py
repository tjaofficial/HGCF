from django.db import models

# Create your models here.
class individualTrees_model(models.Model):
    treeID = models.CharField(max_length=10)
    rootStock = models.CharField(max_length=10)
    zionType = models.CharField(max_length=10)
    datePlanted = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.treeID
    
class locationTree_model(models.Model):
    treeID = models.CharField(max_length=10)
    rootStock = models.CharField(max_length=10)
    zionType = models.CharField(max_length=10)
    datePlanted = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.treeID
    
class areaTree_model(models.Model):
    treeID = models.CharField(max_length=10)
    rootStock = models.CharField(max_length=10)
    zionType = models.CharField(max_length=10)
    datePlanted = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.treeID
    

    