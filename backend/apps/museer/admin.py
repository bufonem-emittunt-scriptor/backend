from django.contrib import admin


from .models import *
# Register your models here.

admin.site.register(Platform)
admin.site.register(Volunteer)
admin.site.register(News)
admin.site.register(BlackList)
admin.site.register(Contacts)
admin.site.register(Event)
admin.site.register(EventSubscription)
admin.site.register(Marks)
admin.site.register(PlatformReviews)
admin.site.register(VolunteerReviews)