from django.contrib import admin
from tweet_app.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname Group', {"fields":["nickname"]}),
        ('Message Group', {"fields":["message"]}),
    ]
    
    # fields = ['nickname']


admin.site.register(Tweet,TweetAdmin)