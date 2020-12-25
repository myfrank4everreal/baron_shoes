from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'baronstore/home.html')



def storeFront(request):
    return render(request, 'baronstore/storefront.html')



# Details functions 

def ultraBoost20(request):
    return render(request, 'baronstore/details/ultraboost20.html')


def newBalace995(request):
    return render(request, 'baronstore/details/newbalace995.html')


def nikeAirforce1(request):
    return render(request, 'baronstore/details/nike_airforce1.html')

def nikePegasus37(request):
    return render(request, 'baronstore/details/nike_pegasus_37.html')


def nikeReact_presto(request):
    return render(request, 'baronstore/details/nike_react_presto.html')