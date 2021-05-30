from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def order(request):
    order_list = ['订单1', '订单2', '订单3']
    return render(request, 'order.html', {'order_list': order_list})

def merch(request):
    merch_list = ['商品1', '商品2', '商品3']
    return render(request, 'merch.html', {'merch_list': merch_list})