from django.shortcuts import render,redirect
from .models import Images,Category,Location
from django.http import Http404

# Create your views here.
def home(request):
    
    return render(request,'index.html')


def gallery(request):
    gallery = Images.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def single_image(request,image_id):
    try:
        image = Images.objects.get(id=image_id)
    except DoesNotExist:
        Http404()
    
    return render(request,'single_image.html',{'gallery':image})

def technology(request):
    tech_cetegory=Category.objects.get(pk=1)
    tech_images=Images.objects.filter(category=tech_cetegory)

    return render(request,'category/technology.html', {"tech_images": tech_images})
    
def nature(request):
    nature_category = Category.objects.get(pk=2)
    nature_images = Images.objects.filter(category=nature_category)

    return render(request,'category/nature.html', {"nature_images": nature_images})

def meditation(request):
    meditation_category = Category.objects.get(pk=3)
    med_images = Images.objects.filter(category=meditation_category)

    return render(request,'category/meditation.html',{"meditation_images": med_images})


def image_location(request):
    nairobi = Location.objects.get(pk=1)#NAIROBI
    karatina  = Location.objects.get(pk=2)
    nyeri = Location.objects.get(pk=3)
    nakuru = Location.objects.get(pk=4)
    mombasa = Location.objects.get(pk=5)
    marsabit = Location.objects.get(pk=6)

    nairobi_images = Images.objects.filter(location=nairobi)
    karatina_images = Images.objects.filter(location=karatina)
    nyeri_images = Images.objects.filter(location=nyeri)
    nakuru_images = Images.objects.filter(location=nakuru)
    mombasa_images = Images.objects.filter(location=mombasa)
    marsabit_images = Images.objects.filter(location=marsabit)

    return render(request, 'location.html', {"nairobi":nairobi_images, "marsabit":marsabit_images, "karatina": karatina_images,"nyeri":nyeri_images,"nakuru":nakuru_images,"mombasa":mombasa_images })


def search_results(request):

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images= Images.search_by_category(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})
    else:

        message = "You have not searched any images"

        return render(request,'search.html',{"message":message})
    
def about(request):
    return render(request,'about.html')