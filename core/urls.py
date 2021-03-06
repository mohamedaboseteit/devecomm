from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", CheckoutForm.as_view(), name="checkout"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),

]

