from rest_framework import serializers

from .models import Pizza, Component, Order, PizzaOrder


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
