from django.urls import path
from .views import RPCInfoView, BundleCreateView, BundleDetailView, TransactionCreateView, CheckHistoryView
from solana_rpc import views

urlpatterns = [
    path('rpc/<str:addr>', RPCInfoView.as_view()),
    path('history', CheckHistoryView.as_view()),
    path('history/<int:ck>', CheckHistoryView.as_view()),
    path('history/nt', CheckHistoryView.as_view()),
    path('bundles', BundleCreateView.as_view()),
    path('bundles/<str:bundle_id>', BundleDetailView.as_view()),
    path('transaction', TransactionCreateView.as_view()),

    path('', views.PublicPageView.as_view(), name='public'),
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('register/rgstrd/', views.RegisterPageView.as_view(), name='register_api'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('home/', views.HomePageView.as_view(), name='home'),
]
