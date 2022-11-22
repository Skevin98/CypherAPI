from django.db import models, transaction
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    description = models.TextField(blank = True)
    profile_img = models.FileField(upload_to='images/profiles/', null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.username


    @transaction.atomic
    def disable(self):
        
        if self.active == False:
            return
        self.active = False
        self.save()

        self.articles.filter(author = self).update(active = False)

    @transaction.atomic
    def enable(self):
        
        if self.active == True:
            return
        self.active = True
        self.save()





class Publication(models.Model):
    title = models.CharField(max_length=191)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    tag = models.CharField(max_length = 191)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-publish_date']

    @transaction.atomic
    def disable(self):
        
        if self.active == False:
            return
        self.active = False
        self.save()



    @transaction.atomic
    def enable(self):
        
        if self.active == True:
            return
        self.active = True
        self.save()


class Article(Publication):
    ARTICLE_TYPES = (
        ('0', 'Other'),
        ('1','Discover'),
        ('2','News'),
        ('3','Topic'),
    )
    content = models.TextField(blank = True)
    author = models.ForeignKey('API.Author', on_delete=models.CASCADE, related_name='articles')
    co_authors = models.ManyToManyField(Author)
    article_type = models.CharField(
        max_length = 20,
        choices = ARTICLE_TYPES,
        default = '0'
        )

    def get_type(self):
        return self.get_article_type_display()

    header_img = models.FileField(upload_to='images/articles/', null=True)

    
    
class Media(Publication):
    MEDIA_TYPES = (
        ('0','Other'),
        ('1','Video'),
        ('2','Music'),
        ('3','Podcast'),
        ('4','Image'),
    )
    
    media_type= models.CharField(
        max_length = 20,
        choices = MEDIA_TYPES,
        default = '0'
    )

    def get_type(self):
        return self.get_media_type_display()

    file=models.FileField(upload_to='media/', null=True)
    header_img = models.FileField(upload_to='images/medias/', null=True)





