from django.urls import path, re_path, include
from .views import box, main, base, base2, base4, post, review, congratulation, review2, review3, review4, review5, card, card2, card3, contact, card4, card5, table, base55, card6, card7, card8, card9, card10, card11, card12, read, message, message2, PostDetailView, pay, PostDetailView2


urlpatterns = [
    path('box/', box),
    path('main/', main),
    path('base/', base, name="base"),
    path('base2/', base2, name="base2"),
    path('base3/', read, name="base3"),
    path('base4/', base4, name="base4"),
    path('contact/', contact, name="base5"),
    path('base55/', base55, name="base55"),
    path('post/', post, name="post"),
    path('review/', review, name="review"),
    path('congratulation/', congratulation, name="congratulation"),
    path('review2/', review2, name="review2"),
    path('review3/', review3, name="review3"),
    path('review4/', review4, name="review4"),
    path('review5/', review5, name="review5"),
    path('boxes/', card, name="card"),
    path('boxes2/', card2, name="card2"),
    path('boxes3/', card3, name="card3"),
    path('boxes4/', card4, name="card4"),
    path('boxes5/', card5, name="card5"),
    path('boxes6/', card6, name="card6"),
    path('boxes7/', card7, name="card7"),
    path('boxes8/', card8, name="card8"),
    path('boxes9/', card9, name="card9"),
    path('boxes10/', card10, name="card10"),
    path('boxes11/', card11, name="card11"),
    path('boxes12/', card12, name="card12"),
    path('boxes12/', card12, name="card12"),
    path('pay/', pay, name="pay"),
    path('message/', message, name="message"),
    path('message2/', message2, name="message2"),
    path('product/<int:pk>/', PostDetailView.as_view(), name="product"),
    path('total/<int:pk>/', PostDetailView2.as_view(), name="total"),

]

