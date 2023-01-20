from django.contrib import admin
from .models import Booking, NowPlaying, Play
#from django_summernote.admin import SummernoteModelAdmin


#class BookingAdmin(SummernoteModelAdmin):
#
 #   summernote_fields = ('time')
 #   list_filter = ('date')
 #   admin.site.register(Booking)

class PlayAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )

    ordering = (
        'name',
    )


class NowPlayingAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'time',
        'play',
        'status',
        'seats',
    )

    ordering = (
        '-date',
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'play',
        'viewing',
        'amount',
        'name',
        'email',
    )

    ordering = (
        '-play',
    )


admin.site.register(Play, PlayAdmin)
admin.site.register(NowPlaying, NowPlayingAdmin)
admin.site.register(Booking, BookingAdmin)