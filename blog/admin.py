from django.contrib import admin
from .models import *

admin.site.register(Blog)
admin.site.register(BlogTag)
admin.site.register(BlogDetail)
admin.site.register(Comment)
admin.site.register(Category)



