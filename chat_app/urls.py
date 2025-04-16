from django.urls import path
from .views import DiagnoseSkinAPIView

urlpatterns = [
    path('diagnose/', DiagnoseSkinAPIView.as_view(), name='diagnose-skin'),
]
