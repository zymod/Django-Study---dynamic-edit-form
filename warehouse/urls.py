from django.urls import path

from . import views

app_name = 'warehouse'

urlpatterns = [
    path('products/', views.product_all_view, name='product_all'),

    path('products/note_edit/', views.product_note_edit)
]
