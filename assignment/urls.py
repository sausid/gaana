from django.urls import path
from assignment.views import LocationListCreateAPIView, LocationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('locations/', LocationListCreateAPIView.as_view(), name='location-list-create'),
    path('locations/<int:id>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name='location-detail'),
]
