from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    publish_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)] )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} stars by {self.user.username} for {self.book.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    favorite_books = models.ManyToManyField(Book, related_name='favored_by')


    def __str__(self):
        return self.user.username