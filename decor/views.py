from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from decor.models import HeaditemModel, ServicesModel, BookingModel,CategoryForGalleryModel,GalleryModel
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    headitems = HeaditemModel.objects.all()
    services = ServicesModel.objects.filter(is_active=True)
    context = {
        "headitems" : headitems,
        "services" : services
    }
    return render(request, 'index.html', context=context)


def detailview(request,namep):
    item = HeaditemModel.objects.get(title=namep)
    context = {
        "item":item
    }
    return render(request, 'detail.html', context=context)

def serviceview(request,namep):
    sevice = ServicesModel.objects.get(title=namep)
    context = {
        "sevice":sevice
    }
    return render(request, "services-single.html", context=context)


def bookview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        description = request.POST.get('describe')
        booking = BookingModel(name=name, phone=phone, description=description)
        booking.save()
        return HttpResponseRedirect(reverse('index'))



def servicesview(request):
    services = ServicesModel.objects.all()
    context = {
        "services": services
    }
    return render(request, 'services.html', context=context)


def contactview(request):
    return render(request, "contact.html")


def aboutusview(request):
    return render(request, "about.html")



def galleryview(request):
    cat = CategoryForGalleryModel.objects.all()
    gallery = GalleryModel.objects.all()
    context = {
        "gallery": gallery,
        "categorys":cat
    }
    return render(request, "galery.html", context=context)

