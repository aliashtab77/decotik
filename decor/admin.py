from django.contrib import admin
from decor.models import HeaditemModel, CategoryModel, ServicesModel, BookingModel,CategoryForGalleryModel, GalleryModel
# Register your models here.

admin.site.register(HeaditemModel)
admin.site.register(CategoryModel)
admin.site.register(ServicesModel)
admin.site.register(BookingModel)
admin.site.register(CategoryForGalleryModel)
admin.site.register(GalleryModel)
