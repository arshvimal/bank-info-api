from django.urls import include, path
from .views import BankList, BranchList, BranchDetail, BankBranches, BankDetail


urlpatterns = [
    path('banks/<pk>/', BankDetail.as_view()),
    path('banks/list', BankList.as_view()),
    path('banks/<bank_id>/branches/', BankBranches.as_view()),
    path('branches/list', BranchList.as_view()),
    path('branches/<pk>/', BranchDetail.as_view()),
]