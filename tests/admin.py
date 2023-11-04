from django.contrib import admin

from .models import Test, Word, Lang

# Register your models here.
admin.site.register(Test)
admin.site.register(Word)
admin.site.register(Lang)