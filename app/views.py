from django.shortcuts import render

from . models import UseProduct

def activeProduct(request):
    products = UseProduct.objects.filter(isReturn=False)
    inproducts = UseProduct.objects.filter(isReturn=True)

    for i in products:
        print('Company Name :', i.employe.companyName)
        print('Employee Name:', i.employe)
        print('Product Name: ', i.product)
        print('Product Taken Time: ', i.takenTime)
        print('Product Return Time: ', i.returnTime)
        print('----------------')

    return render(request, 'index.html', {'products': products, 'inproducts': inproducts})
