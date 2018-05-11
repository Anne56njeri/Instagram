from django.conf.urls import url,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^$',views.index,name='Index'),
url(r'^accounts/',include('registration.backends.simple.urls')),
url(r'^profile/',views.first_profile,name='Profile'),
url(r'^images/',views.add_image,name='Image'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
