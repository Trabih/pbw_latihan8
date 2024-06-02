from django.urls import path
from .views import *

urlpatterns = [
    path('journals/', JournalList.as_view(), name='journal-list'),
    path('updatejournals/<int:pk>/', JournalUpdate.as_view(), name='journal-update'),
    path('deletejournals/<int:pk>/', JournalDelete.as_view(), name='journal-delete'),
    path('hitungderet/', HitungDeret.as_view(), name='hitung-deret'),
]
