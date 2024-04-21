from django.urls import path
from .views import RequestCreate, RequestList, Requestupdate

urlpatterns = [
    path('submit-request/', RequestCreate.as_view(), name="request_submit"),
    path('my-requests/', RequestList.as_view(),name='my_requests'),
    path('update_request/<int:pk>/', Requestupdate.as_view(),name='update_request'),
]