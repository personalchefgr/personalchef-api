from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    # API routes
    path('v1/', include([
        path('contact-form/', include('contact_form.urls')),
        path('coupons/', include('coupons.urls')),
        path('dietary-plans/', include('dietary_plans.urls')),
        path('newsletter/', include('newsletter.urls')),
        path('orders/', include('orders.urls')),
        path('payments/', include('payments.urls')),
        path('postcode-areas/', include('postcode_areas.urls')),
        path('pricing-plans/', include('pricing_plans.urls')),
        path('subscriptions/', include('subscriptions.urls')),
        path('users/', include('users.urls')),
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
