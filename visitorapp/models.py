from django.db import models


class BinanceKey(models.Model):
    """Model with api's keys, cryptocurrencies and markets"""
    api = models.CharField(max_length=65)
    secret = models.CharField(max_length=65)


class Currency(models.Model):
    """ Model for crypto currency with name and symbol """
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=3)
    position = models.IntegerField(db_index=True, default=0)


class Bank(models.Model):
    name = models.CharField(db_index=True, max_length=5)
    amount_currency_one = models.FloatField()
    amount_currency_two = models.FloatField()
    amount_currency_three = models.FloatField()


class Bot(models.Model):
    is_working = models.BooleanField(default=False)


class Market(models.Model):
    symbol = models.CharField(max_length=6)
    position = models.IntegerField(db_index=True, default=0)


class Order(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    side = models.CharField(max_length=4)
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    is_completed = models.BooleanField(default=False)


class Trade(models.Model):
    open_date = models.DateTimeField(db_index=True, auto_now_add=True)
    closed_date = models.DateTimeField(default="")
    order_one = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="trade_order_one")
    order_two = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="trade_order_two")
    order_three = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="trade_order_three")
    is_completed = models.BooleanField(db_index=True, default=False)
