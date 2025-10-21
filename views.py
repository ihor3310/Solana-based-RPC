from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rpc_api.models import HistoryOfAllRequests
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
from .models import RegistrationRequest

from solana.rpc.api import Client
from solders.pubkey import Pubkey
import json

class HomePageView(TemplateView):
    template_name = 'home.html'


class RegisterPageView(TemplateView):
    template_name = 'register.html'
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('email')
            password = data.get('password')
            
            registration = RegistrationRequest.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            
            return JsonResponse({'success': True, 'id': registration.id}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


class LoginPageView(TemplateView):
    template_name = 'login.html'


class PublicPageView(TemplateView):
    template_name = 'public.html'





class CheckHistoryView(APIView):
    def get(self, request):
        items = HistoryOfAllRequests.objects.all().values('last_request', 'count', 'note')
        for_json_history = list(items)
        return Response(for_json_history)

    def delete(self, request, ck):
        type_to_del = HistoryOfAllRequests.objects.get(count=ck)
        try:
            type_to_del.delete()
            return Response({'id': ck, 'delete': 'passed'})
        except:
            return Response({'id': ck, 'delete': 'failed'})

    def patch(self, request):
        body = json.loads(request.body)
        ck = body["id_number"]
        nt = body["note"]
        note_add_change = HistoryOfAllRequests.objects.get(count=ck)
        note_add_change.note = nt
        try:
            note_add_change.save()
            return Response({'changed_note': nt})
        except:
            return Response({'change': 'failed'})

class RPCInfoView(APIView):
    def get(self, request, addr):
        client = Client("https://api.mainnet-beta.solana.com")
        public_key = Pubkey.from_string(addr)
        response = client.get_balance(public_key)
        response_lamp = response.value
        response_sol = response.value / 1_000_000_000

        last_item = HistoryOfAllRequests.objects.last()
        if last_item is not None and last_item.count is not None:
            new_cnt = last_item.count + 1
        else:
            new_cnt = 1
        new_req = HistoryOfAllRequests.objects.create(last_request="rpcInfoType", count=new_cnt)

        return Response({
            "wallet_balance_in_lamports": response_lamp,
            "wallet_balance_in_sol": response_sol,
        })

class BundleCreateView(APIView):
    def post(self, request):

        last_item = HistoryOfAllRequests.objects.last()
        if last_item is not None and last_item.count is not None:
            new_cnt = last_item.count + 1
        else:
            new_cnt = 1
        new_req = HistoryOfAllRequests.objects.create(last_request="bundleCreateType", count=new_cnt)

        return Response({
            "bundle_id": "test-uuid-123",
            "status": "pending",
            "created_at": "2025-10-07T12:00:00Z"
        }, status=status.HTTP_201_CREATED)

class BundleDetailView(APIView):
    def get(self, request, bundle_id):

        last_item = HistoryOfAllRequests.objects.last()
        if last_item is not None and last_item.count is not None:
            new_cnt = last_item.count + 1
        else:
            new_cnt = 1
        new_req = HistoryOfAllRequests.objects.create(last_request="bundleCheckType", count=new_cnt)

        return Response({
            "bundle_id": bundle_id,
            "status": "confirmed",
            "slot": 123456,
            "transactions": ["sig1", "sig2"]
        })

class TransactionCreateView(APIView):
    def post(self, request):

        last_item = HistoryOfAllRequests.objects.last()
        if last_item is not None and last_item.count is not None:
            new_cnt = last_item.count + 1
        else:
            new_cnt = 1
        new_req = HistoryOfAllRequests.objects.create(last_request="TransCreateType", count=new_cnt)

        return Response({
            "signature": "5j7s6NiJS3JAkvgkoc18WVAsiSaci2pxB2A6ueCJP4tprA2TFg9wSyTLeYouxPBJEMzJinENTkpA52YStRW5Dia7",
            "status": "pending"
        }, status=status.HTTP_201_CREATED)
