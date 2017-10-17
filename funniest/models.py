import base64
import gc
import os

import django
from django import forms
from django.conf import settings
from django.contrib import admin
from django.db import models
from django.core.cache import cache


class SweetStoreOrder(models.Model):
    order_id = models.IntegerField(default=1, help_text='sample order')

    def create_sweet_store_order(self, order_id):
        self.order_id = order_id
        self.save()


class SweetStoreOrderAdmin(admin.ModelAdmin):
    from django.db import models
    formfield_overrides = {
        models.ImageField: {'widget': forms.FileInput},
    }
    list_display = ('order_id',)
    list_filter = ['order_id']
