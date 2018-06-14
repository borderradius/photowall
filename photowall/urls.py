from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts/', include('accounts.urls'), # blog와는 다르게 accounts 에서는 namespce를 사용하지 않는다. 왜냐하면 auth 앱내에서 namespce를 사용하지않고 url reserve 기능을 사용하고 있기 때문.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)