from django.contrib import admin

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic

# Register your models here.

admin.site.register(RevenueStatistic)
admin.site.register(SpendStatistic)
