from rest_framework.generics import ListAPIView
from main_app.api.serializers import RevenueStatisticReadSerializer, SpendStatisticReadSerializer
from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from rest_framework import viewsets
from django.db.models import Q, Sum, Subquery, OuterRef, DecimalField


class RevenueStatisticViewSet(ListAPIView):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticReadSerializer

    def get_queryset(self):
        query_date = self.request.query_params.get('date')
        query_name = self.request.query_params.get('name')

        if query_date and query_name:
            return self.queryset.filter(Q(date=query_date) & Q(name=query_name)).annotate(
                Sum("revenue"), Sum("spend__spend"), Sum("spend__impressions"), Sum("spend__clicks"),
                Sum("spend__conversion"))
        else:
            return self.queryset.filter()


class SpendStatisticticViewSet(ListAPIView):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticReadSerializer

    def get_queryset(self):
        query_date = self.request.query_params.get('date')
        query_name = self.request.query_params.get('name')

        if query_date and query_name:
            revenue_subquery = RevenueStatistic.objects.filter(spend=OuterRef("pk")).values("revenue")[:1]
            return self.queryset.filter(Q(date=query_date) & Q(name=query_name)).annotate(
                Sum("spend"), Sum("impressions"), Sum("clicks"), Sum("conversion"),
                revenue=Sum(Subquery(revenue_subquery), output_field=DecimalField()))
        else:
            return self.queryset.filter()
