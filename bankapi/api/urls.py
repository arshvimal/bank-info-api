from django.urls import include, path
from .views import BankList, BranchList, BranchDetail, BankBranches, BankDetail


urlpatterns = [
    path('', BankList.as_view()),
    path('<pk>/', BankDetail.as_view()),
    path('branches/', BranchList.as_view()),
    path('branches/<pk>/', BranchDetail.as_view()),
    path('<bank_id>/branches/', BankBranches.as_view()),
]