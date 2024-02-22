from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        # Calculate the average rating for the product
        average_rating = self.reviews.aggregate(Avg('stars'))['stars__avg']
        if average_rating is not None:
            return round(average_rating, 2)  # Round to 2 decimal places
        else:
            return None  # Return None if there are no reviews

class ProductReview(models.Model):
    """
    A model for users to rate and reviews books, and for users
    to see ratings and reviews from all other users
    """
    class Meta:
        ordering = ['-date_added']

    STAR_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STAR_CHOICES)
    content = models.TextField(blank=True, null=True, max_length=3000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    # @receiver(post_save, sender=ProductReview)
    # def update_rating_on_save(sender, instance, created, **kwargs):
    #     instance.product.rating = instance.product.get_rating()
    #     instance.product.save()


    # @receiver(post_delete, sender=ProductReview)
    # def update_rating_on_delete(sender, instance, *args, **kwargs):
    #     instance.product.rating = instance.product.get_rating()
    #     instance.product.save()
