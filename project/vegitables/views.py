from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from vegitables.models import Product,Cart,Order
from django.db.models import Q
import razorpay
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')



def register(request):
    context={}
    if request.method=="GET":
        return render(request,'register.html')
    else:
        name=request.POST['uname']
        email=request.POST['umail']
        password=request.POST['upass']
        cpassword=request.POST['ucpass']

       
        if name=="" or email=="" or password=="":
            context['errmsg']="Field can not be blank"
        elif password != cpassword:
            context['errmsg']="Password and confirm password must be same"
        elif len(password)<8:
            context['errmsg']="Password should contain atleast 8 characters"
        else:
            u=User.objects.create(username=name,email=email)
            u.set_password(password)
            u.save()
            #return HttpResponse("data reached ")
            return redirect('/login')
        

def product(request):
    # print(request.user.id)
    p=Product.objects.filter(is_active=True)
    print(p)
    
    context={}
    context['data']=p
    print(context)
    return render(request,'index.html',context)
    print('i reached here')


def vegetables(request):
    p=Product.objects.filter(is_active=True)
    print(p)
    
    context={}
    context['data']=p
    return render(request,'vegetables.html',context)

def addtocart(request,pid):
    #  print('product id is:',pid)
    #  print('user id is: ',request.user.id)
    context={}
    if request.user.is_authenticated:
        print("User is logged in")
        u=User.objects.filter(id=request.user.id)
        p=Product.objects.filter(id=pid)
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])

        c=Cart.objects.filter(q1 & q2)
        context['data']=p
        if len(c)!=0:
            context['errmsg']="Product Already Exist..!!"
            return render(request,'vegetables.html',context)
        else:
            c=Cart.objects.create(uid=u[0],pid=p[0],amt=p[0].price)
            c.save()
            
            context['success']="Product Added to Cart Successfully..!!"
            return render(request,'vegetables.html',context)
    else:
        #print("User is not logged in")
        return redirect('/login')
    
def viewcart(request):
    c=Cart.objects.filter(uid=request.user.id)
    print(c)
    context={}
    context['data']=c
    s=0
    for i in c:
        s=s + i.pid.price * i.qty 

    context['subtotal']=s
    context['n']=len(c)
    return render(request,'cart.html',context)

        
def user_login(request):
    context={}
    if request.method=='GET':
        return render(request,'login.html')
    else:

        un=request.POST['uname']
        up=request.POST['password']

        '''print(un)
        print(up)'''
        u=authenticate(username=un,password=up)
        #print(u)
        if u==None:
            #print("invailed Credentails ")
            context['errmsg']="Invalid Credentails"
            return render(request,'login.html',context)
        else:
            #print("User login successfully")
            login(request,u)
            return redirect('/product')
        #return HttpResponse("Credentials checked")

def  user_logout(request):
    logout(request)
    return redirect('/login')

def updateqty(request,x,cid):
    c=Cart.objects.filter(id=cid)
    q=c[0].qty
    print(type(x))
    if x=='1':
        q=q+1
    elif q>1:
        q=q-1

    c.update(qty=q)
    return redirect('/cart')

def removecart(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/cart')

def contact(request):
    return render(request,'contact.html')

def fruits(request):
    p=Product.objects.filter(is_active=True)
    print(p)
    
    context={}
    context['data']=p
    return render(request,'fruits.html',context)

def nonveg(request):
    p=Product.objects.filter(is_active=True)
    print(p)
    
    context={}
    context['data']=p
    return render(request,'non-veg.html',context)

def fetchorder(request):
    o=Cart.objects.filter(uid=request.user.id)
    print(o)
    context={}
    context['data']=o
    s=0
    for i in o:
        s = s + i.amt

    context['total']=s

    context['n']=len(o)
    return render(request,'checkout.html',context)

# def offer(request):
#     off=request.POST['code']
#     print(off)

def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_HeYv5uvRUwSNEa", "FKsfWPzm770aRcJaLCP1tSOh"))

    o=Cart.objects.filter(uid=request.user.id)
    print('price',o[0].amt)
    s=0
    for i in o:
        s = s + i.amt

    data = { "amount": s*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    #print(payment)
    context={}
    context['payment']=payment
    return render(request,'pay.html',context)

def success(request):
    u=User.objects.filter(id=request.user.id)
    to=u[0].email
    sub='Frutables Order Status'
    frm='Abhishekyadav@gmail.com'
    msg='Your order has been placed successfully..!!'
    send_mail(
        sub,
        msg,
        frm,
        [to],
        fail_silently=False
    )

    return render(request,'success.html')