from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('indexBack', views.indexBack, name="indexBack"),
    path('blog-5/', views.blog5, name="blog5"),
    path('cart/', views.cart, name="cart"),
    path('lostPassword/', views.lostPassword, name="lostPassword"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('error-404/', views.error404, name="error404"),
    path('login_view/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout'),
    path('products-left-sidebar-2/', views.productLeftSideBar2, name="productLeftSideBar2"),
    path('products-type-1/', views.productsType1, name="productsType1"),
    path('signup/', views.signup, name="signup"),
    path('single-blog-1/', views.singleBlog1, name="singleBlog1"),
    path('track-order/', views.trackOrder, name="trackOrder"),
    path('allUsersBack/', views.allUsersBack, name="allUsersBack"),
    path('blog5Back/', views.blog5Back, name="blog5Back"),
    path('categoriesBack/', views.categoriesBack, name="categoriesBack"),
    path('contactBack/', views.contactBack, name="contactBack"),
    path('ordersBack/', views.ordersBack, name="ordersBack"),
    path('productLeftSideBar2Back/', views.productLeftSideBar2Back, name="productLeftSideBar2Back"),
    path('profileBack/', views.profileBack, name="profileBack"),
    path('update_contact_info/', views.update_contact_info, name='update_contact_info'),
    path('delete/<int:id>', views.delete_category, name='delete_category'),
    path('update_category/<int:id>/', views.update_category, name='update_category')
]
