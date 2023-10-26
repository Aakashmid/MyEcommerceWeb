from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='Shop home'),
    path("about/",views.about,name='About'),
    path("contact/",views.contact,name='Contact'),
    path("search/",views.search,name='Search'),
    path("products/<int:myid>",views.productview,name='View Product'),
    path("tracker/",views.tracker,name='Traker'),
    path("checkout/",views.checkout,name='Checkout'),
]
