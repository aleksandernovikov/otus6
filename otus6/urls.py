from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('course-list')), name='index'),
    path('admin/', admin.site.urls),
    path('university/', include('university.urls')),
    path('contacts/', include('contacts.urls')),
    path('api/v1/', include('api.urls'))
]
