from django.db import models

# Create your models here.
class Product_Category(models.Model):
    Pc_Id=models.IntegerField(primary_key=True)
    Pc_Name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Pc_Name
    

class Product(models.Model):
    Pc_Name=models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    P_Id=models.IntegerField(primary_key=True)
    P_Name=models.CharField(max_length=100)
    P_Price=models.IntegerField()
    P_Description=models.TextField()
    P_Date=models.DateField()

    def __str__(self) -> str:
        return self.P_Name
