from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .detail.detailModels import detail
from .test.testModels import test

admin.site.register(detail)
admin.site.register(test)
