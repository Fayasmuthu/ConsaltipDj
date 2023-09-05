from django.shortcuts import render ,redirect
from .models import BlogPost,Tag,gallery_photo,boxform
from .models import ContactMessage,Comment
from .forms import ContactForm , CommentForm
from django.contrib import messages
# from .models import EmailSubscription
# from .forms import EmailSubscriptionForm


import json
from django.http import JsonResponse

# Create your views here.

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def about(request):
    # Your view logic here
    context ={
        "is_about" : True
    }
    return render(request, 'details/about.html' , context)

def index2(request):
    context ={
        "is_index" : True
    }
    # Your view logic here
    return render(request, 'details/index-2.html' , context)




def project(request):
    # Your view logic here
    return render(request, 'details/project.html')

def blog(request):

    posts = BlogPost.objects.all()
    tags = Tag.objects.all()
    context={
        'posts': posts,
        'tags': tags,
        "is_blogs" : True
    }
    # Your view logic here
    return render(request, 'details/blog.html',context)

def contact(request):

    if request.method == 'POST':
            name=request.POST.get('name')
            emailC=request.POST.get('email')
            phone=request.POST.get('number')
            service=request.POST.get('choice')
            message=request.POST.get('message')

            contact_1=ContactMessage(
                full_name=name,
                email=emailC,
                phone_number=phone,
                service=service,
                message=message
            )
            contact_1.save()

    context ={
        "is_contacts" : True
    }
    return render(request, 'details/contact.html', context)

def project_details(request):
    # Your view logic here
    
    return render(request, 'details/project-details.html')

def blog_details(request):
    # Your view logic here
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_details')  # Redirect to a view that displays the list of comments
    else:
        form = CommentForm()
    return render(request, 'details/blog-details.html',{'form': form})

def index3(request):
    # Your view logic here
    return render(request, 'details/index-3.html')

def index4(request):
    # Your view logic here
    return render(request, 'details/index-4.html')

def faq(request):
    # Your view logic here
    context ={
        "is_faqs" : True
    }
    return render(request, 'details/faq.html' , context)

def found(request):
    # Your view logic here
    return render(request, 'details/not-found.html')
def service(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success message or redirection here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/service.html', {'form': ContactForm()})
            # ...
    else:
        form = ContactForm()
    box = boxform.objects.all()
    
    context = {
        'form': form,
        'box' : box,
        "is_services": True
        }
   
    return render(request, 'details/service.html',context)

def service_details(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add success message or redirection here
            messages.success(request, 'Thank you for your message!')
            return render(request, 'details/service.html', {'form': ContactForm()})
            # ...
    else:
        form = ContactForm()

    context = {
        'form': form,
        
        }

    # form = ContactForm()  # Initialize the contact form

    # if request.method == 'POST':
    #     form_type = request.POST.get("formhidden")

    #     if form_type == "ewt": 
    #         form = ContactForm(request.POST)
        
    #         if form.is_valid():
    #             form.save()

    #             # Show a success message
    #             messages.success(request, 'Thank you for your message!')

    #             # Clear the form for a new submission
    #             form = ContactForm()

    #     elif form_type == "formemail":
    #         email_form = EmailSubscriptionForm(request.POST)

    #         if email_form.is_valid():
    #             email = email_form.cleaned_data['email']

    #             # Check if the email already exists in subscriptions
    #             if not EmailSubscription.objects.filter(email=email).exists():
    #                 EmailSubscription.objects.create(email=email)
    #                 messages.success(request, "Thank you for subscribing!")
    #             else:
    #                 messages.warning(request, "You are already subscribed!")

    # context = {
    #     'form': form,
    # }
    
    return render(request, 'details/service-details.html', context)

def team(request):
    # Your view logic here
    return render(request, 'details/team.html')

def dollar(request):
    # Your view logic here
    return render(request, 'details/$.html')

def gallery(request):
    # Your view logic here
    photo = gallery_photo.objects.all()
    context={
        'photo':photo,
        "is_gallerys": True
    }
    return render(request, 'details/gallery.html',context)

def tag(request):
    # Your view logic here
    return render(request, 'blog/tags.html')

def search(request):
    # Your view logic here
    return render(request, 'blog/search.html')

def paginations(request):
    # Your view logic here
    return render(request, 'blog/paginations.html')



def form_fields(request):
    # Your view logic here
    return render(request, 'details/form_fields.html')