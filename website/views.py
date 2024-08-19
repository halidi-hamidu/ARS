from django.shortcuts import render

# Create your views here.

def homePage(request):
    template_name = 'website/index.html'
    context = {

    }
    return render( request, template_name, context)

def properties(request):
    template_name = 'website/properties.html'
    context={}
    return render( request, template_name, context)

def about(request):
    template_name = 'website/about.html'
    context={}
    return render( request, template_name, context)
def contact(request):
    template_name = 'website/contact.html'
    context={}
    return render( request, template_name, context)

def team(request):
    template_name = 'website/team.html'
    context={}
    return render( request, template_name, context)

def blog(request):
    template_name = 'website/blog.html'
    context={}
    return render( request, template_name, context)

def testimonials(request):
    template_name = 'website/testimonials.html'
    context={}
    return render( request, template_name, context)

def terms(request):
    template_name = 'website/terms.html'
    context={}
    return render( request, template_name, context)