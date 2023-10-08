from django.db import models


class StockRecord(models.Model):
    product = models.ForeignKey('catalog.product', on_delete=models.CASCADE, related_name="stockrecords")
    sku = models.CharField(max_length=64, unique=True, null=True, blank=True)
    buy_price = models.PositiveBigIntegerField(null=True, blank=True)
    sale_price = models.PositiveBigIntegerField()
    num_stock = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Stock Record"
        verbose_name_plural = "Stock Records"
