from django.shortcuts import render
from first_app.models import Projects

# Create your views here.
def index(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/index.html', context = my_dict)

def skills(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/myself1.html', context = my_dict)


def portfolio(reqest):
    my_list = Projects.objects.order_by('title')
    proj_dict = {'projects' : my_list}
    return render(reqest, 'first_app/mywork.html', context = proj_dict)


def blog(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/myedu.html', context = my_dict)


def social(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/myfamily.html', context = my_dict)



def gallary(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/myedu.html', context = my_dict)

def contact(reqest):
    my_dict = {'inser_content' : 'Hello I am Sandeep Gaur '}
    return render(reqest, 'first_app/myedu.html', context = my_dict)
