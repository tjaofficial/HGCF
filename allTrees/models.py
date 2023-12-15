from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

meal_type_choices = (
    ('dessert', 'Dessert'),
    ('dinner-main', 'Dinner - Main'),
    ('dinner-side', 'Dinner - Side'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('brunch', 'Brunch'),
    ('quick snack', 'Quick Snack'),
)    
yes_no_choice = (
    ("yes","Yes"),
    ("no","No"),
)

class locationTree_model(models.Model):
    locationID = models.CharField(max_length=10)
    name = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    dateEst = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.locationID
    
class areaTree_model(models.Model):
    areaID = models.CharField(max_length=10)
    locationID = models.ForeignKey(locationTree_model, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    widthByTree = models.IntegerField()
    lengthByTree = models.IntegerField()
    dateEst = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.locationID) + " - " + str(self.areaID)

class individualTrees_model(models.Model):
    treeID = models.CharField(max_length=20)
    areaID = models.ForeignKey(areaTree_model, on_delete=models.CASCADE, blank=True, null=True)
    locationID = models.ForeignKey(locationTree_model, on_delete=models.CASCADE, blank=True, null=True)
    rootStock = models.CharField(max_length=10)
    zionType = models.CharField(max_length=10)
    datePlanted = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.locationID) + " - " + str(self.areaID.areaID) + " - " + str(self.treeID)

class logCategory_model(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.name
    
class treeLogs_model(models.Model):
    treeID = models.ForeignKey(individualTrees_model, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    note = models.CharField(max_length=10000)
    category = models.ForeignKey(logCategory_model, on_delete=models.CASCADE)
    def __str__(self):
        return self.treeID.treeID + ' - ' + self.category.name + ' - ' + str(self.date) + '-' + str(self.time)
    
class tree_qr(models.Model):
    treeID = models.OneToOneField(
        individualTrees_model,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    url = models.CharField(max_length=300)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.treeID)
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB', (400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.treeID}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)

class recipeModel(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.JSONField()
    equipment = models.JSONField()
    serving_size = models.IntegerField(
        null=True,
        blank=True
    )
    time = models.CharField(max_length=20)
    meal_type = models.CharField(
        max_length=60,
        choices=meal_type_choices
    )
    directions = models.TextField(max_length=20000)
    special_notes = models.CharField(
        max_length=2000,
        null=True,
        blank=True
    )
    healthy_choice = models.CharField(
        max_length=7,
        choices=yes_no_choice
    )
    def __str__(self):
        return str(self.id) + " - " + str(self.name)