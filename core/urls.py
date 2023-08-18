# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("", include("apps.requests.urls")),
    path("", include("apps.home.urls")),
    path("", include("apps.api.urls"))
]
