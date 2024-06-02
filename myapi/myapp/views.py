from django.shortcuts import render
from .models import *
from rest_framework import generics, views
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status



def journal_list(request):
    journals = Journal.objects.all()
    token_key =''
    if request.user.is_authenticated:
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        token_key = token.key

    context = {
        'journals': journals,
        'token' :token_key
    }
    return render(request, 'journal_list.html', context)

class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

class JournalUpdate(generics.UpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

    
class JournalDelete(generics.DestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]


def deret_angka(awal, akhir):
    hasil = list(range(awal, akhir + 1, 1))
    return hasil

class HitungDeret(views.APIView):
    def post(self, request):

        data = request.data
        awal = data.get('awal')
        akhir = data.get('akhir')

        if not awal or not akhir:
            return Response({"error": "Nilai Parameter Harus Diisi"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            hasil_deret = deret_angka(awal, akhir)
            total = sum(hasil_deret)
            return Response({"hasil_deret": hasil_deret, "total": total}, status=status.HTTP_200_OK)


