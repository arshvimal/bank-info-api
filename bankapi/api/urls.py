from django.urls import include, path
from .views import BankList, BranchList, BranchDetail, BankBranches, BankDetail


urlpatterns = [
    path('bank/<pk>/', BankDetail.as_view()),
    path('bank/list/', BankList.as_view()),
    path('bank/<bank_id>/branches/', BankBranches.as_view()),
    path('branch/list/', BranchList.as_view()),
    path('branch/<pk>/', BranchDetail.as_view()),
]