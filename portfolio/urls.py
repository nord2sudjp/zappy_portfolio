from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('penpo/admin/', admin.site.urls),
    path('penpo/', jobs.views.home, name='home'),
    path('penpo/job/', jobs.views.home, name='jobs.urlhome'),
    path('penpo/blog/', include('blog.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
      + static(settings.CSS_URL, document_root=settings.CSS_ROOT) \
      + static(settings.SCRIPT_URL, document_root=settings.SCRIPT_ROOT)
