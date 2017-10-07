from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{class_name} Name: {name}".format(class_name=self.__class__.__name__,
                                                  name=self.__getattribute__('name'))

    class Meta:
        abstract = True


class Pizza(BaseModel):
    name = models.CharField(
        max_length=250
    )
    components = models.ManyToManyField(
        'Component'
    )
    price = models.IntegerField()
    is_active = models.BooleanField(
        default=False
    )
    image = models.ImageField(
        null=True
    )


class Component(BaseModel):
    name = models.CharField(
        max_length=250
    )
    price = models.IntegerField()


class Order(models.Model):
    statuses = (
        ('C', 'Cancelled'),
        ('S', 'Start'),
        ('A', 'Accepted'),
        ('R', 'Realization'),
        ('P', 'Provider'),
        ('E', 'Ended')
    )
    price = models.IntegerField()
    pizzas = models.ManyToManyField(
        Pizza, through='PizzaOrder'
    )
    client = models.ForeignKey(
        User
    )

    date_created = models.DateTimeField(
        auto_created=True,
        auto_now=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )

    status = models.CharField(
        max_length=1,
        choices=statuses,
        default='S'
    )

    def __str__(self):
        return "{class_name} Id: {name}".format(class_name=self.__class__.__name__, name=self.id)


class PizzaOrder(models.Model):
    order = models.ForeignKey(
        Order
    )
    pizza = models.ForeignKey(
        Pizza
    )
    count = models.IntegerField(
        default=1
    )
