from django.shortcuts import render,HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
from django.contrib import messages
from datetime import datetime
import json

# Create your views here.
def searchMatch(query,item):
    if query in item.desc.lower() or query in item.category.lower() or query in item.product_name.lower():
        return True
    else:
        return False
def home(request):
    Products=Product.objects.all() # Collect all records from table
    # n=len(Products)
    # nslides=n//4 + ceil((n/4)-(n//4)) 
    # params={"Products":Products,"no_of_slides":nslides,'range':range(1,nslides)}
    alprod=[]
    # alprod=[[Products,range(1,nslides),nslides],
    #         [Products,range(1,nslides),nslides]]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4)-(n//4)) 
        alprod.append([prod,range(1,nslides),nslides])
    params={"alprods":alprod}
    return render(request,'shop/index.html',params)

# Function for handlig search items
def search(request):
    Products=Product.objects.all() # Collect all records from table
    query=request.GET.get('searchitem') # Getting what user search
    
    # print(query)
    alprod=[]

    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prod)
        nslides=n//4 + ceil((n/4)-(n//4)) 

        if n!=0:  
            alprod.append([prod,range(1,nslides),nslides])
    params={"alprods":alprod}
    if len(alprod)==0 or len(query)<3:
        params={"msg":"There something wrong please search rlevant item"}
    # if 1!=2:
    #     params={}
    #     return render(request,'shop/search.html',params)
    
    return render(request,'shop/search.html',params)
def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Details submitted !!")
        submit=True
        return render(request,'shop/contact.html',{'submit':submit})

    return render(request,'shop/contact.html')

def productview(request,myid):
    product=Product.objects.filter(id=myid)
    # print(product)
    return render(request,'shop/productview.html',{'product':product[0]})
def tracker(request):
    if request.method=="POST":
        order_id=request.POST.get('orderId','')
        email=request.POST.get('email','')
      
        
        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps({'status':'success','updates':updates,'item_json':order[0].items_json},default=str)
                    
                
                return HttpResponse(response)

                
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse(f"{e}")
            
    return render(request,'shop/tracker.html')

#Fetching value for order table
def checkout(request):
    
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        items_json=request.POST.get('itemsJson','')
        address=request.POST.get('Address1') + " " + request.POST.get('Address2')
        phone=request.POST.get('Phone')
        state=request.POST.get('State')
        city=request.POST.get('City')
        zip_code=request.POST.get('Zip')
        amount=request.POST.get('amount','')
        order=Order(name=name,items_json=items_json,email=email,phone=phone,state=state,city=city,address=address,zip_code=zip_code,amount=amount)
        order.save()
        orderupdate=OrderUpdate(order_id=order.order_id,update_desc="Your order is placed")
        orderupdate.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
       

    return render(request,'shop/checkout.html')