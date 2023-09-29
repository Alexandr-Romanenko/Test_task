from django.urls import path, include
from main_app.api.resourses import RevenueStatisticViewSet, SpendStatisticticViewSet


urlpatterns = [
    path('', include(router.urls)),
    path('revenue/', RevenueStatisticViewSet.as_view()),
    path('spend/', SpendStatisticticViewSet.as_view()),
    ]



