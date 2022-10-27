from django.contrib import admin
from .models import Lomba, DetailLomba, Voting

# Register your models here.
admin.site.register(Lomba)
admin.site.register(DetailLomba)
admin.site.register(Voting)