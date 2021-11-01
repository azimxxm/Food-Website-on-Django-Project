from django.db import models


class Our_Specialty(models.Model):
    title = models.CharField(max_length=50, null=True)
    info = models.TextField(max_length=255, null=True)
    icon = models.ImageField(upload_to="Icons/",  null=True)
    images = models.ImageField(upload_to="Images/",  null=True)
    data_created = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mutaxassisligimiz"
        verbose_name_plural = "Mutaxassisligimiz"


class Orders(models.Model):
    name = models.CharField(max_length=50, null=True)
    price_1 = models.FloatField(default=0.0, null=True)
    price_2 = models.FloatField(default=0.0, null=True)
    images = models.ImageField(upload_to="Images/",  null=True)
    data_created = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taomlar"
        verbose_name_plural = "Taomlar"


class Gallarey(models.Model):
    title = models.CharField(max_length=50, null=True)
    info = models.TextField(max_length=255, null=True)
    images = models.ImageField(upload_to="Images/",  null=True)
    data_created = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Galareya"
        verbose_name_plural = "Galareya"


class Received_Orders(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    food_name = models.CharField(max_length=100, null=True)
    adress = models.TextField(max_length=300, null=True)
    is_published = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Received_Orders"
        verbose_name_plural = "Received_Orders"


class Comments(models.Model):
    name = models.CharField(max_length=50, null=True)
    images = models.ImageField(upload_to="Comment/",  null=True)
    commant = models.TextField(max_length=250, null=True)
    is_published = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comments"