from django.shortcuts import render
from AppFreeMarket.models import Buyer, Seller, Delivery
from django.http import HttpResponse
from AppFreeMarket.forms import BuyerForm, SellerForm, DeliveryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def buyer(request):
    return render(request, 'buyer.html')

def seller(request):
    return render(request, 'seller.html')

def delivery(request):
    return render(request, 'delivery.html')

def buyers(request):
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

def sellers(request):
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

def deliveries(request):
    if request.method == 'POST':
        myForm = DeliveryForm(request.POST)

        print(myForm)

        if myForm.is_valid:

            info = myForm.cleaned_data
            deivery = Delivery(name=info['name'], number=info['number'], delivered=info['delivered'])
            deivery.save()
            return render(request, 'home.thml')
    else:
        myForm = DeliveryForm()
    
    return render(request, 'delivery.html', {'myForm':myForm})

def searchDelivery(request):
    return render(request, 'searchDelivery.html')

def search(request):
    if request.GET['delivery']:
        delivery = request.GET['delivery']
        name = Delivery.onjects.filter(delivery__icontains=delivery)

        return render(request, 'home.html', {'delivery':delivery})
    else:
        response = f'No information to show.'
    return render(request, 'inicio.html', {'response':response})



