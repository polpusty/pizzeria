from django.conf.urls import url, include

from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'pizzas', views.PizzaViewSet)

urlpatterns = [
    url(r'^orders/add/', views.add_order,
        name='add_order'),
    url(r'^orders/list/', views.list_orders,
        name='list_orders'),
    url(r'^orders/edit/(?P<order_id>[0-9])/$', views.editing_order,
        name='edit_order'),
    url(r'^orders/detail/(?P<order_id>[0-9])/$', views.details_order,
        name='details_order'),
    url(r'^orders/action/add_pizza_to_order/(?P<order_id>[0-9])/$', views.add_pizza_to_order,
        name='add_pizza_to_order'),
    url(r'^orders/action/change_status_order/(?P<order_id>[0-9])/$', views.change_status_order,
        name='change_status_order'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^', views.home,
        name='home'),
]
