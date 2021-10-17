from django.db import models
from django.conf import settings
# Create your models here.


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'исполнен'),
        (CANCEL, 'отменен'),
    )
    userName = models.CharField(verbose_name="Имя ", max_length=64, blank=False)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=False)
    status = models.CharField(verbose_name='Статус', 
                              max_length=3,
                              choices=ORDER_STATUS_CHOICES, 
                              default=FORMING)
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание заказа")
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True, null=True)