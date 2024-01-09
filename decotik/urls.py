"""
URL configuration for decotik project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static
from decor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path("project/<str:namep>",views.detailview,name='detailview'),
    path("services/<str:namep>",views.serviceview,name='servieview'),
    path("addbook",views.bookview,name='bookview'),
    path("services",views.servicesview,name='servicesview'),
    path("contactus",views.contactview,name='contactview'),
    path("gallery",views.galleryview,name='galleryview'),
    path("aboutus",views.aboutusview,name='aboutusview')
]
if settings.IS_DEVEL:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
