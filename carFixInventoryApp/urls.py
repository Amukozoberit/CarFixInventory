from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from carFixInventoryApp import views

urlpatterns = [
    path('inventoryView/', views.InventorySnippetList.as_view()),
    path('inventoryView/<int:pk>', views.InventorySnippetDetail.as_view()),
    path('mechanicsandservicesview/', views.MechanicViewSet.as_view({'get': 'list'})),
    path('mechanicandservicespost/', views.MechanicViewSet.as_view({'post': 'create'})),
    path('serviceview/', views.ServiceViewSet.as_view({'get': 'list'})),
    path('servicepost/', views.ServiceViewSet.as_view({'post': 'create'})),

]

urlpatterns = format_suffix_patterns(urlpatterns)