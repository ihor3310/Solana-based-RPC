from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RPCInfoView(APIView):
    def post(self, request):
        return Response({
            "jsonrpc": "2.0",
            "result": {"context": {"slot": 123456}, "value": 500000000},
            "id": request.data.get('id', 1)
        })

class BundleCreateView(APIView):
    def post(self, request):
        return Response({
            "bundle_id": "test-uuid-123",
            "status": "pending",
            "created_at": "2025-10-07T12:00:00Z"
        }, status=status.HTTP_201_CREATED)

class BundleDetailView(APIView):
    def get(self, request, bundle_id):
        return Response({
            "bundle_id": bundle_id,
            "status": "confirmed",
            "slot": 123456,
            "transactions": ["sig1", "sig2"]
        })

class TransactionCreateView(APIView):
    def post(self, request):
        return Response({
            "signature": "5j7s6NiJS3JAkvgkoc18WVAsiSaci2pxB2A6ueCJP4tprA2TFg9wSyTLeYouxPBJEMzJinENTkpA52YStRW5Dia7",
            "status": "pending"
        }, status=status.HTTP_201_CREATED)