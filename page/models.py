from django.db import models
from autoslug import AutoSlugField

#     ******    status de ilk kısım database kayıt ismi ikinci kısım ise biizim admin panelde göreceğmiz kısım  ********
#default status diye bir değişken tanımlayıp aşağıda kullanmak için yaptık yazmak zoounda değildik ama yapalım dedik
DEFAULT_STATUS='draft'

STATUS= [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]

class Page(models.Model):
    title=models.CharField(max_length=150)  
    slug = models.SlugField(max_length=150,default="")
    content=models.TextField()
    cover_image=models.ImageField(upload_to="page",
        null=True,
        blank=True,
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#classlar arası en az 2 boşluk olacak

class Carousel(models.Model):
    title=models.CharField(max_length=150,blank=True,null=True)  
    cover_image=models.ImageField(upload_to="carousel",
        null=True,
        blank=True,
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
