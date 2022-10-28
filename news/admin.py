from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(OfficialArticle)
admin.site.register(UMKMArticle)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Subscribe)