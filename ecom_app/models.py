from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    changefreq = models.CharField(max_length=10, choices=[
        ('always', 'Always'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('never', 'Never')
    ], default='weekly')
    priority = models.FloatField(default=0.5)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/%s" % self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    # image = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    changefreq = models.CharField(max_length=10, choices=[
        ('always', 'Always'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('never', 'Never')
    ], default='daily')
    priority = models.FloatField(default=0.7)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/%s" % self.name
class Products(models.Model):
    id_num = models.IntegerField(primary_key=True)
    # img_url = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    # photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    sub_category = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_at = models.DateTimeField(auto_now=True)  # Updated every time the record is saved
    name = models.CharField(max_length=100, null=True)
    specification = models.CharField(max_length=500, null=True, blank=True)
    price = models.FloatField(null=True)
    # base = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    changefreq = models.CharField(max_length=10, choices=[
        ('always', 'Always'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('never', 'Never')
    ], default='daily')
    priority = models.FloatField(default=0.9)
    def __str__(self):
        return self.sub_category

    def get_absolute_url(self):

        # return self.created_at
        # return f"/product/{self.category}/{self.id_num}/"
        return "/product/%s/%i/" % (self.sub_category, self.id_num)





