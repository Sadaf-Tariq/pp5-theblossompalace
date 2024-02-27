from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def average_rating(self) -> float:
        return Rating.objects.filter(recipe_id=self).aggregate(Avg("rating"))["rating__avg"] or 0


class Rating(models.Model):
    """
    A rating model to rate recipe by users
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(
        blank=False,
        default=0,
        validators=[field_validation, MaxValueValidator(5.0)])

    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"
