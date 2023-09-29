from rest_framework import serializers
from revenue.models import RevenueStatistic
from spend.models import SpendStatistic


class SpendStatisticReadSerializer(serializers.ModelSerializer):    
    revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)

    class Meta:
        model = SpendStatistic
        fields = ('name', 'date', 'spend', 'impressions', 'clicks', 'conversion', 'revenue')
        read_only_fields = ('id', 'name', 'date', 'spend', 'impressions', 'clicks', 'conversion')


class RevenueStatisticReadSerializer(serializers.ModelSerializer):    
    spend = SpendStatisticReadSerializer()    

    class Meta:
        model = RevenueStatistic
        fields = ('name', 'spend', 'date', 'revenue')
        read_only_fields = ('id', 'name', 'spend', 'date', 'revenue')

