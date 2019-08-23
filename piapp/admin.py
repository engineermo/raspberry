from django.contrib import admin
from .models import PiFour

# Register your models here.
class PiFourAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":("css/admin/extraadmin.css",)
        }
admin.site.register(PiFour, PiFourAdmin)

admin.site.site_header = "EDUŞ Cooking Blog"
admin.site.site_title = "Afiyet olsun."
admin.site.index_title = "Welcome to the best Turkish food"