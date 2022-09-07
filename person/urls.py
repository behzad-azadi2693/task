from django.urls import path
from .views import PersonCreateView, index
from api.api_check import check_field

app_name = 'person'

urlpatterns = [
    path('', PersonCreateView.as_view(), name='person_create_view'),
    path('check_field/<str:field>/', check_field, name="check_field"),
]