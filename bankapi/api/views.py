from django.shortcuts import render
from .models import Banks, Branches
from rest_framework import generics
from .serializers import BanksSerializer, BranchesSerializer

# Create your views here.
class BankList(generics.ListAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer

class BankDetail(generics.RetrieveAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer

class BankBranches(generics.ListAPIView):
    serializer_class = BranchesSerializer

    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        return Branches.objects.filter(bank_id=bank_id)

class BranchList(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

class BranchDetail(generics.RetrieveAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

