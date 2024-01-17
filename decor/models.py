from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "دسته بندی اسلاید شو"
    def __str__(self):
        return f"{self.name}"
class HeaditemModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to="headitems/")
    address = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="headitems")
    duration = models.CharField(max_length=255)
    class Meta:
        verbose_name = "آیتم های اسلاید شو"
    def __str__(self):
        return f"{self.title}"



class ServicesModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    avatar = models.ImageField(upload_to="sevices")
    is_active = models.BooleanField(default=False)
    project_done = models.IntegerField(default=0)
    project_inhand = models.IntegerField(default=0)
    class Meta:
        verbose_name = "خدمات"
    def __str__(self):
        return f"{self.title}"


class BookingModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "رزرو ها"
    def __str__(self):
        return f"{self.name} --> {self.phone}"



class CategoryForGalleryModel(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = "دسته بندی های گالری"
    def __str__(self):
        return f"{self.name}"


class GalleryModel(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryForGalleryModel, on_delete=models.CASCADE, related_name="category1")
    image = models.ImageField(upload_to="galleries/")
    class Meta:
        verbose_name = "گالری"
    def __str__(self):
        return f"{self.name} - {self.category}"


