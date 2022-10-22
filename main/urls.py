from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from account.views import LoginView
from mainpage.views import index, product_detail, login_user

from category.views import CategoryViewSet
from product.views import ProductViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
# router.register('login', LoginView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('home/', index),
    path('home/<str:id>/', product_detail, name='product-detail'),
    # path('home/<str:id>', login_user, name='login-user'),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/orders/', include('order.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
