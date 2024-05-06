from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Model: Category
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)  # Defines a character field with a max length of 250 characters that must be unique across all category instances
    slug = models.SlugField(max_length=250, unique=True)  # Similar to `name`, but used for URL paths. Needs to be unique
    description = models.TextField(blank=True)  # Text field for category descriptions that allows empty values
    image = models.ImageField(upload_to='category', blank=True)  # Image field where uploaded images will be stored in the 'category' directory and can be left blank

    class Meta:
        ordering = ('name',)  # This meta option specifies the default ordering of query results to sort by name alphabetically.
        verbose_name = 'category'  # Human-readable single name for Category objects, used in the Django admin.
        verbose_name_plural = 'categories'  # Human-readable plural name for Category objects.
    
    def get_category(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name  # Returns the string representation of the model, which is the category name


# Model: Product
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)  # Defines a character field for the product name, must also be unique
    slug = models.SlugField(max_length=250, unique=True)  # URL-friendly identifier for the product, also unique
    description = models.TextField(blank=True)  # Large text field for product descriptions, allows empty values
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Cretaes a many-to-one relationship with Category. If a Category is deleted, all associated Products will be deleted
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field to store product prices, up to 10 digits in total, with 2 decimal places
    image = models.ImageField(upload_to='product', blank=True)  # An image field for product images, stored in the 'product' directory, optionally blank
    stock = models.IntegerField()  # An integer field to keep track of product stock levels
    available = models.BooleanField(default=True)  # A boolean field to indicate whether the product is available for sale; Defaults = True.
    created = models.DateTimeField(auto_now_add=True)  # A datetime field that records when the product instance was created. Automatically set when object is first created.
    updated = models.DateTimeField(auto_now=True)  # A datetime field that records the last time the product instance was updated. Automatically updated every time the object is saved.
    
    class Meta:
        ordering = ('name',)  # Orders Product objects by name alphabetically.
        verbose_name = 'product'  # Singular name for Product in the admin interface.
        verbose_name_plural = 'products'  # Plural name for Product in the admin interface.

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name  # String representation of the Product, typically used in the Django admin and in debug messages.
