from django.shortcuts import render
from first_app.models import Projects, blog

# Create your views here.
def index(request):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(request, 'first_app/index.html', context = my_dict)

def skills(request):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(request, 'first_app/skills.html', context = my_dict)


def portfolio(request):
    my_list = Projects.objects.order_by('title')
    proj_dict = {'projects' : my_list}
    return render(request, 'first_app/portfolio.html', context = proj_dict)


def my_blog(request):
    my_blogs = blog.objects.all()
    my_blog_dict = {'blogs' : my_blogs}
    return render(request, 'first_app/blog.html', context = my_blog_dict)


def social(request):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(request, 'first_app/social.html', context = my_dict)



def gallary(request):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(request, 'first_app/gallary.html', context = my_dict)

def contact(request):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(request, 'first_app/contact.html', context = my_dict)
