from django.contrib import admin
from .models import UserProfile, Interest, Match, SubscriptionPlan,Report


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved', 'district', 'place')
    list_filter = ('is_approved', 'district', 'place')
    # Add more fields to customize the list view
    
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['user', 'interest_user', 'timestamp']
    
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['user', 'match_user', 'timestamp']

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'reported_user', 'reason', 'timestamp']