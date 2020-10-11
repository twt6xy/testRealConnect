  
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('realConnectSite/index.html')
    return render(request, 'realConnectSite/index.html')


def account_page(request):
    template = loader.get_template('realConnectSite/accountPage.html')
    return render(request, 'realConnectSite/accountPage.html')

def rep_page(request):
    template = loader.get_template('realConnectSite/repPage.html')
    return render(request, 'realConnectSite/repPage.html')