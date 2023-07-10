from django.db import models

from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=70
    )
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))
    note = models.TextField(
        _('Note'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    def __str__(self):
        return self.name
    
