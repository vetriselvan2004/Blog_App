from django.shortcuts import *
from django.urls import reverse

def custom_page_not_found(request,exception):
 return render(request,'404.html' , status=404)