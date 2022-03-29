"""lab6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# from stocks import views as stock_views
from django.urls import include, path
from stocks import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cars', views.DonutViewSet)
router.register(r'carssets', views.DonutsSetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('set/<int:id>',  views.set, name='set'),
    path('set_add/', views.set_add, name='set_add'),
    path('set_edit/<int:id>', views.set_edit, name='set_edit'),
    path('set_delete/<int:id>', views.set_delete, name='set_delete'),
    path('set/car_add/<int:id>', views.donut_add, name='donut_add'),
    path('car_edit/<int:id>', views.donut_edit, name='donut_edit'),
    path('car_delete/<int:id>', views.donut_delete, name='donut_delete'),

    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()