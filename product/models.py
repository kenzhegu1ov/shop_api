from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    @property
    def reviews(self):
        return self.review_set.all()

    def __str__(self):
        return self.title


STAR_CHOICES = (
    (1, "* "),
    (2, 2 * "* "),
    (3, 3 * "* "),
    (4, 4 * "* "),
    (5, 5 * "* "),
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
