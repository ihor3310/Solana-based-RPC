from django.urls import path
from .views import RPCInfoView, BundleCreateView, BundleDetailView, TransactionCreateView

urlpatterns = [
    path('info', RPCInfoView.as_view()),
    path('bundles', BundleCreateView.as_view()),
    path('bundles/<str:bundle_id>', BundleDetailView.as_view()),
    path('transaction', TransactionCreateView.as_view()),
]