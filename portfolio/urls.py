from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path(settings.HOME_URL + 'admin/', admin.site.urls),
    # path(r'/penpo/' , jobs.views.home, name='home'),
    path(settings.HOME_URL , jobs.views.home, name='home'),
    path(settings.HOME_URL + 'job/', jobs.views.home, name='jobs.urlhome'),
    path(settings.HOME_URL + 'blog/', include('blog.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
      + static(settings.CSS_URL, document_root=settings.CSS_ROOT) \
      + static(settings.SCRIPT_URL, document_root=settings.SCRIPT_ROOT)
