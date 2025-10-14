from django.urls import path
from .views import RPCInfoView, BundleCreateView, BundleDetailView, TransactionCreateView, CheckHistoryView

urlpatterns = [
    path('rpc/<str:addr>', RPCInfoView.as_view()),
    path('history', CheckHistoryView.as_view()),
    path('history/<int:ck>', CheckHistoryView.as_view()),
    path('history/nt', CheckHistoryView.as_view()),
    path('bundles', BundleCreateView.as_view()),
    path('bundles/<str:bundle_id>', BundleDetailView.as_view()),
    path('transaction', TransactionCreateView.as_view()),
]
