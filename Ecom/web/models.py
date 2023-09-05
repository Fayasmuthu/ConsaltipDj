from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    name =models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class gallery_photo(models.Model):
    image =models.ImageField(upload_to='gallery/img')

from django.db import models

class ServiceMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    optionC = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.created_at}"


class boxform(models.Model):
    ICON_CHOICES = (
        ('icon-project-manangement', 'project Icon'), 
        ('icon-process-development', 'process Icon'),
        ('icon-commitment', 'commitment Icon'),
        ('icon-human-resources', 'Human Icon'),
        ('icon-operation', 'operation Icon'),
        ('icon-business-analysis', 'Business Icon'), 
    
    )
    spanclassname = models.CharField(max_length=200, choices=ICON_CHOICES)
    name =models.CharField(max_length=200)
    title =models.CharField(max_length=200)

