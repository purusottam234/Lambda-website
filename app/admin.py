from app.models import FAQ, Service,Team,Category,Listing
from django.contrib import admin

# Register your models here.
admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(Team)
admin.site.register(Listing)
admin.site.register(Category)