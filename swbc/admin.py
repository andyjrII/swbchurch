from django.contrib import admin
from .models import NewsEvent, Sermon, Service

admin.site.register(NewsEvent)
admin.site.register(Sermon)
admin.site.register(Service)