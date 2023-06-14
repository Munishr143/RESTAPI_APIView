from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
#from django.http import HttpResponse

# def Sample(request):
#     LOP=Product.objects.all()
#     print(LOP)
#     for po in LOP:
#         if po.P_Name=='Toys':
#             print(po.P_Price)
#     return HttpResponse('The data is successfully sent')

class ProductCrud(APIView):
    def get(self, request, P_Id):
        PQS=Product.objects.all()
        PJD=ProductMS(PQS, many=True)
        return Response(PJD.data)
    
    def post(self, request, P_Id):
        PMSD=ProductMS(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'Product of {} is Created'.format(SPO.P_Id)})
        else:
            return Response({'failed': 'Product Creation is Failed'})
        
    def put(self, request, P_Id):
        P_Id=request.data['P_Id']
        PO=Product.objects.get(P_Id=P_Id)
        UPO=ProductMS(PO, data=request.data)
        if UPO.is_valid():
            SPO=UPO.save()
            return Response({'message':'Product of {} is Updated'.format(SPO.P_Id)})
        else:
            return Response({'failed': 'Product Updation is Failed'})
        
    def patch(self, request, P_Id):
        # P_Id=request.data['P_Id']
        # PO=Product.objects.get(P_Id=P_Id)
        # PO.P_Name=request.data.get('P_Name', PO.P_Name)
        # PO.P_Price=request.data.get('P_Price', PO.P_Price)
        # PO.P_Description=request.data.get('P_Description', PO.P_Description)
        # PO.P_Date=request.data.get('P_Date', PO.P_Date)
        # PO.Pc_Name=request.data.get('Pc_Name', PO.Pc_Name)
        # PO.save()
        # # UPO=Product.objects.filter(P_Id=P_Id).update(P_Price=P_Price)
        # return Response({'message':'Product is Updated'})

        P_Id=request.data['P_Id']
        PO=Product.objects.get(P_Id=P_Id)
        UPO=ProductMS(PO, data=request.data, partial=True)
        if UPO.is_valid():
            SPO=UPO.save()
            return Response({'message':'Product of {} is Updated'.format(SPO.P_Id)})
        else:
            return Response({'failed': 'Product Updation is Failed'})
    
    def delete(self, request, P_Id):
        PO=Product.objects.filter(P_Id=P_Id)
        if PO:
            PO.delete()
            return Response({'message':'Product is Deleted'})
        else:
            return Response({'message':'No Product is there'})

