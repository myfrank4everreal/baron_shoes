
from django.urls import path
from . import views 



urlpatterns = [
        path('', views.homePage, name='home'),
        path('storefront', views.storeFront, name='store'),

        # details views
        path('ultraboost20', views.ultraBoost20, name='ultraboost20'),
        path('newBalace995', views.newBalace995, name='newbalace995'),
        path('nike_Air_force1', views.nikeAirforce1, name='nike_air_force1'),
        path('nike_pegasus37', views.nikePegasus37, name='nikepagasus37'),
        path('nike_react_presto', views.nikeReact_presto, name='nike_react_presto'),

        # top 10 new balance sneaker for 2020



        # Five best airjordan sneaker


        


]

