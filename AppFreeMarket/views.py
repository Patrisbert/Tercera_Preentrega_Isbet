from django.shortcuts import render
from AppFreeMarket.models import Buyer, Seller, Delivery
from django.http import HttpResponse
from AppFreeMarket.forms import BuyerForm, SellerForm, DeliveryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(self):
    product=Delivery(name="item", number=13245)
    product.save()
    
    textDoc = f'---> Delivery: {product.name} number: {product.number}'
    return HttpResponse(textDoc)

def buyer(request):
    if request.method == 'POST':
        myForm = BuyerForm(request.POST)

        print(myForm)

        if myForm.is_valid:

            info = myForm.cleaned_data
            buyer = Buyer(name=info['name'], surname=info['surname'], email=info['email'])
            buyer.save()
            return render(request, 'home.thml')
    else:
        myForm = BuyerForm()
    
    return render(request, 'buyer.html', {'myForm':myForm})

def seller(request):
    if request.method == 'POST':
        myForm = SellerForm(request.POST)

        print(myForm)

        if myForm.is_valid:

            info = myForm.cleaned_data
            seller = Seller(name=info['name'], surname=info['surname'], email=info['email'])
            seller.save()
            return render(request, 'home.thml')
    else:
        myForm = SellerForm()
    
    return render(request, 'seller.html', {'myForm':myForm})

def delivery(request):
    if request.method == 'POST':
        myForm = DeliveryForm(request.POST)

        print(myForm)

        if myForm.is_valid:

            info = myForm.cleaned_data
            product = Delivery(name=info['name'], number=info['number'])
            product.save()
            return render(request, 'home.thml')
    else:
        myForm = DeliveryForm()
    
    return render(request, 'delivery.html', {'myForm':myForm})

def searchDelivery(request):
    return render(request, 'searchDelivery.html')

def search(request):
    if request.GET['number']:
        number = request.GET['number']
        product = Delivery.objects.filter(number__icontains=number)

        return render(request, 'home.html', {'product':product, 'number':number})
    else:
        response = f'No information to display.'
    return render(request, 'home.html', {'response':response})
