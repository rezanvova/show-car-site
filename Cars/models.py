from django.db import models
from django.utils.text import slugify

def translit_to_eng(s: str):
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))



class Car(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, verbose_name="Description")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=False)
    popularity = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, related_name='posts', verbose_name="Категории",
                            null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name="Теги")

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    @property
    def avg_rating(self):
        if self.rating_count > 0:
            return round(self.popularity/self.rating_count,2)
        return 0

    class Meta:
        pass

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/models/category/{self.slug}"

class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/models/tag/{self.slug}"


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')