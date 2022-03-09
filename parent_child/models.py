from django.db import models


# Parent Table
class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=95)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = 'Parents'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


# Child Table
class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

