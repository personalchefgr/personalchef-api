from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('dietary-plans/', include('dietary_plans.urls')),
        path('pricing-plans/', include('pricing_plans.urls')),
        path('subscriptions/', include('subscriptions.urls')),
        path('contact-form/', include('contact_form.urls')),
        path('postcode-areas/', include('postcode_areas.urls')),
        path('users/', include('users.urls')),
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
