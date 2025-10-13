from django.urls import path
from .views import RPCInfoView, BundleCreateView, BundleDetailView, TransactionCreateView, CheckHistiryView

urlpatterns = [
    path('rpc/<str:addr>', RPCInfoView.as_view()),
    path('history', CheckHistiryView.as_view()),
    path('history/<int:ck>', CheckHistiryView.as_view()),
    path('history/nt', CheckHistiryView.as_view()),
    path('bundles', BundleCreateView.as_view()),
    path('bundles/<str:bundle_id>', BundleDetailView.as_view()),
    path('transaction', TransactionCreateView.as_view()),
]
