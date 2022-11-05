from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # /advocates
    path('advocates/', views.advocates),
    # /advocate/username
    path('advocates/<str:username>/', views.advocate),
    # /companies
    path('companies/', views.companies),
    # /companies/id
    path('companies/<int:id>', views.company),
]