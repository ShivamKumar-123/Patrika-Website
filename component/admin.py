# admin.py
from django.contrib import admin
from .models import AllCards,Members, NewArrival, FeedBack

class MembersAdmin(admin.ModelAdmin):
    list_display = ("name","position","description")

class AllCardsAdmin(admin.ModelAdmin):
    list_display = ("name","description","type")

class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ("name","description","type")


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("name","email","message","date_added")

admin.site.register(Members,MembersAdmin)

admin.site.register(AllCards,AllCardsAdmin)

admin.site.register(NewArrival,NewArrivalAdmin)

admin.site.register(FeedBack,FeedBackAdmin)