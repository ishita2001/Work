from django.shortcuts import render, redirect
from .models import *
from web.forms import(
    BuyerRegistrationForm,
    SellerRegistrationForm,
    LoginForm,
    BuyerEditProfileForm,
    SellerEditProfileForm,
    ProductForm,
    CommentForm,
    EditProductForm
)
from django.http import HttpResponse
from django.contrib.auth import(
    login,
    logout,
    authenticate,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

loggedin = 'false'

def buyer_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('web:login_index')

    else:
        if request.method == 'POST':
            form = BuyerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('web:login_index')
        else:
            form = BuyerRegistrationForm()
        return render(request,'web/buyersignup.html',{'form':form})


def seller_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('web:login_index')

    else:
        if request.method == 'POST':
            form = SellerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('web:login_index')
        else:
            form = SellerRegistrationForm()
        return render(request,'web/sellersignup.html',{'form':form})        

def login_view(request):
        
        global loggedin

        if loggedin is 'true':
            return redirect('web:login_index')
    
        else:    
            if request.method == 'POST':
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    user = form.get_user()
                    loggedin = 'true'
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('web:login_index') 

            else:
                form = LoginForm()
            return render(request, 'web/login.html', {'form':form})

@login_required(login_url='/web/login/')
def my_profile(request):
    return render(request, 'web/myprofile.html',{'user':request.user})

@login_required(login_url='/web/login/')
def edit_profile(request):

    if request.user.is_buyer is True:
        if request.method == 'POST':
            form = BuyerEditProfileForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('web:my_profile')

        else:
            form = BuyerEditProfileForm(instance=request.user)
        return render(request, 'web/editprofile.html',{'form':form})

    else:
        if request.method == 'POST':
            form = SellerEditProfileForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('web:my_profile')

        else:
            form = SellerEditProfileForm(instance=request.user)
        return render(request, 'web/editprofile.html',{'form':form})
    
def edit_details(request,pk):
    user = request.user
    product = user.products.get(pk=pk)

    if request.method == 'POST':
        form = EditProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'web/productdetails.html',
                         {'user': request.user,
                          'product':user.products.get(pk=pk),
                         })

    else:
        form = EditProductForm(instance=product)
    return render(request, 'web/edit_details.html',
                 {'user': request.user,
                  'product':user.products.get(pk=pk),
                  'form':form
                 })

@login_required(login_url='/web/login/')
def login_index(request):
    if request.user.is_seller is True:
        return render(request, 'web/seller_loggedin.html')
    else:
        return render(request, 'web/buyer_loggedin.html')

@login_required(login_url='/web/login/')
def logout_view(request):
    global loggedin
    if request.method == 'POST':
        loggedin = 'false'
        logout(request)
        return redirect('web:home')

def home(request):

    categories = Category.objects.all()
    global loggedin

    if loggedin is 'true':
        return redirect('web:login_index',{'categories':categories})

    else:
        return render(request, 'web/homepage.html')

def signup_options(request):
    return render(request, 'web/options.html')

@login_required(login_url='/web/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('web:my_profile')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'web/changepassword.html',{'form':form})

@login_required(login_url='/web/login/')
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.image = request.FILES['image']
            product.save()
            return redirect('web:product_create_view')
    else:
        form = ProductForm()
    return render(request, "web/product_create.html",{'form':form})

def product(request,pk):
    user = request.user
    product = user.products.get(pk=pk)
    return render(request, 'web/productdetails.html',
        {   'user': request.user,
            'product':user.products.get(pk=pk),
        })


@login_required(login_url='/web/login/')
def view_wishlist(request):
    user = request.user
    buyer = Buyer.objects.get(user=request.user)
    return render(request, 'web/wishlist.html',{'buyer': buyer})


@login_required(login_url='/web/login/')
def add_to_wishlist(request, pk):
    user = request.user
    buyer = Buyer.objects.get(user=request.user)
    product = Product.objects.get(pk = pk)
    buyer.wishlist.add(product)
    return render(request, 'web/productdetails.html', {'product':Product.objects.get(pk=pk)})

@login_required(login_url='/web/login/')
def remove_wishlist(request, pk):
    user = request.user
    buyer = Buyer.objects.get(user=request.user)
    product = Product.objects.get(pk = pk)
    buyer.wishlist.remove(product)
    return render(request, 'web/wishlist.html', {'buyer': buyer})

@login_required(login_url='/web/login/')
def search_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.item = product
            comment.save()
            # request.session['temp_data'] = form.cleaned_data
    else:
        form = CommentForm()
    return render(request, 'web/productdetails.html',
        {'product':Product.objects.get(pk=pk),'form':form})

# def product_in_category(request, pk):
#     category = Category.objetcs.get(pk=pk)
#     return render(request, 'web/category_wise.html',{'category':Category.objetcs.get(pk=pk)})
    

    
# Create your views here.
