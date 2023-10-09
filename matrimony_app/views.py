from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout  # Rename the auth.logout function

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import SubscriptionPlan

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import SubscriptionPlan

import json
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscriptionPlan  # Update with the actual import

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscriptionPlan

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscriptionPlan

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscriptionPlan

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscriptionPlan

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from.models import *
# Create your views here.
def index(request):
    return render(request,'home/index.html')


def signup(request):
    # Get the district and place choices from the UserProfile model
    district_choices = UserProfile.DISTRICT_CHOICES
    place_choices = UserProfile.PLACE_CHOICES
    
    # Get the sibling choices and marital status choices from the UserProfile model
    sibling_choices = UserProfile.SIBLING_CHOICES
    marital_choices = UserProfile.MARITAL_STATUS_CHOICES
    
    context = {
        'district_choices': district_choices,
        'place_choices': place_choices,
        'sibling_choices': sibling_choices,
        'marital_choices': marital_choices,
    }
    
    return render(request, 'home/signup.html', context)

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')


from django.core.paginator import Paginator
from .models import UserProfile

def admin_home(request):
    all_users = UserProfile.objects.all()
    paginator = Paginator(all_users, 4)  # Display 4 users per page
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    context = {'users': users}
    return render(request, 'admin/admin_home.html', context)


from .models import SubscriptionPlan

from django.shortcuts import render
from .models import UserProfile

from django.shortcuts import render
from .models import UserProfile  # Import your UserProfile model here

# user_home view
from django.contrib import messages

def user_home(request):
    # Get the gender of the logged-in user
    user_gender = request.user.userprofile.gender
    
    # Determine the opposite gender
    opposite_gender = 'female' if user_gender == 'male' else 'male'
    
    # Filter profiles based on the opposite gender and approval status
    opposite_gender_profiles = UserProfile.objects.filter(gender=opposite_gender, is_approved=True)
    
    # Fetch all distinct districts
    district_choices = UserProfile.objects.values_list('district', flat=True).distinct()
    
    # Fetch other available choices (education, religion, and age range)
    education_choices = UserProfile.EDUCATION_CHOICES
    religion_choices = UserProfile.RELIGION_CHOICES
    age_range_choices = [
        ('20-25', '20 to 25'),
        ('25-30', '25 to 30'),
        ('30-35', '30 to 35'),
        # Add more age range choices as needed
    ]
    
    # Check if the user has a subscription
    has_subscription = SubscriptionPlan.objects.filter(user=request.user.userprofile).exists()
    
    if not has_subscription:
        messages.error(request, "You do not have an active subscription. Please subscribe to access this feature.")
    
    context = {
        'opposite_gender_profiles': opposite_gender_profiles,
        'education_choices': education_choices,
        'religion_choices': religion_choices,
        'district_choices': district_choices,
        'age_range_choices': age_range_choices,
    }

    return render(request, 'user/user_home.html', context)





from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import UserProfile

def registration(request):
    default_image = settings.STATIC_URL + 'static/ice.png'

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        education = request.POST.get('education')
        selected_course = request.POST.get('selected_course')
        job = request.POST.get('job')
        worked_at = request.POST.get('worked_at')
        religion = request.POST.get('religion')
        caste = request.POST.get('caste')
        district = request.POST.get('district')
        place = request.POST.get('place')
        profile_picture = request.FILES.get('profile_picture')
        photo_1 = request.FILES.get('photo_1')
        photo_2 = request.FILES.get('photo_2')
        photo_3 = request.FILES.get('photo_3')
        photo_4 = request.FILES.get('photo_4')
        height = request.POST.get('height')
        age = request.POST.get('age')
        mob = request.POST.get('mob')
        date_of_birth = request.POST.get('date_of_birth')
        marital_status = request.POST.get('marital_status')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        mother_job = request.POST.get('mother_job')  # Added field
        father_job = request.POST.get('father_job')  # Added field
        male_siblings = request.POST.get('male_siblings')  # Added field
        female_siblings = request.POST.get('female_siblings')  # Added field
        married_male_siblings = request.POST.get('married_male_siblings')  # Added field
        married_female_siblings = request.POST.get('married_female_siblings')  # Added field

        about = request.POST.get('about')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('index')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        member = UserProfile.objects.create(
            user=user,
            date_of_birth=date_of_birth,
            address=address,
            education=education,
            selected_course=selected_course,
            job=job,
            worked_at=worked_at,
            religion=religion,
            caste=caste,
            district=district,
            place=place,
            gender=gender,
            profile_picture=profile_picture,
            photo_1=photo_1,
            photo_2=photo_2,
            photo_3=photo_3,
            photo_4=photo_4,
            height=height,
            age=age,
            mob=mob,
            marital_status=marital_status,
            mother_name=mother_name,
            father_name=father_name,
            mother_job=mother_job,
            father_job=father_job,
            about=about,
            male_siblings=male_siblings,
            female_siblings=female_siblings,
            married_male_siblings=married_male_siblings,
            married_female_siblings=married_female_siblings
        )

        custom_user_id = f"member{member.id:04}"
        member.custom_user_id = custom_user_id
        member.save()

        subject = 'Welcome to Matrimony'
        message = f'Thank you for joining our Matrimony. Your registration as a member was successful. We look forward to working with you.\n\nYour username: {username}\nYour password: {password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, "Registration successful. You can't log in until your account is approved by the admin.")
        return redirect('index')
    else:
        context = {
            'default_image': default_image,
            'education_choices': UserProfile.EDUCATION_CHOICES,
            'religion_choices': UserProfile.RELIGION_CHOICES,
            'caste_choices': UserProfile.CASTE_CHOICES,
            'district_choices': UserProfile.DISTRICT_CHOICES,
            'place_choices': UserProfile.PLACE_CHOICES,
            'marital_status_choices': UserProfile.MARITAL_STATUS_CHOICES,
            'SIBLING_CHOICES': UserProfile.SIBLING_CHOICES,  
            }
        return render(request, 'home/signup.html', context)





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Admin logged in successfully!')
                return render(request, 'admin/admin_home.html')  # Replace with your admin home template
            elif hasattr(user, 'userprofile') and user.userprofile.is_approved:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return render(request, 'user/user_home.html')  # Replace with your user home template
            elif hasattr(user, 'userprofile') and not user.userprofile.is_approved:
                message = "Your registration has not been approved yet."
                return render(request, 'home/admin_aprove.html', {'approval_message': message})
            else:
                message = "Your registration has not been completed."
                return render(request, 'home/index.html', {'incomplete_registration_message': message})
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, 'home/index.html')

    return render(request, 'home/index.html')


# Rename your view to something different
def logout(request):
    auth_logout(request)
    return redirect('index')

def user_profiles(request):
    # Retrieve all user profiles from the database
    user_profiles = UserProfile.objects.all()

    context = {
        'user_profiles': user_profiles
    }

    return render(request, 'admin/user_profiles.html', context)


def view_profile(request):
    now = timezone.now()
    user_profile = UserProfile.objects.get(user=request.user)

    user_photo_urls = {
        'photo_1': user_profile.photo_1.url if user_profile.photo_1 else None,
        'photo_2': user_profile.photo_2.url if user_profile.photo_2 else None,
        'photo_3': user_profile.photo_3.url if user_profile.photo_3 else None,
        'photo_4': user_profile.photo_4.url if user_profile.photo_4 else None,
    }

    education_choices = UserProfile.EDUCATION_CHOICES
    district_choices = UserProfile.objects.values_list('district', flat=True).distinct()
    age_range_choices = [
        ('20-25', '20 to 25'),
        ('25-30', '25 to 30'),
        ('30-35', '30 to 35'),
    ]    
    religion_choices = UserProfile.RELIGION_CHOICES

    subscriptions = SubscriptionPlan.objects.filter(user=user_profile)
    
    context = {
        'user_profile': user_profile,
        'subscriptions': subscriptions,  # Add subscriptions to the context
        'user_photo_urls': user_photo_urls,
        'education_choices': education_choices,
        'district_choices': district_choices,
        'age_range_choices': age_range_choices,
        'religion_choices': religion_choices,
        'now': now, 
    }
    
    return render(request, 'user/view_profile.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile

def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    education_choices = UserProfile.EDUCATION_CHOICES
    
    
    course_choices = {
        'high_school': [
            'Mathematics',
            'English',
            'Science',
            'Social Studies',
            'History',
            'Others'
        ],
        'associate_degree': [
            'Business Administration',
            'Computer Science',
            'Engineering',
            'Criminal Justice',
            'Healthcare Management',
            'Others'
        ],
        'bachelors_degree': [
            'Psychology',
            'Marketing',
            'Biology',
            'Economics',
            'Political Science',
            'Others'
        ],
        'masters_degree': [
            'MBA',
            'Computer Science',
            'Education',
            'Public Health',
            'Fine Arts',
            'Others'
        ],
        'doctorate': [
            'Ph.D. in Psychology',
            'Doctor of Medicine (MD)',
            'Doctor of Law (JD)',
            'Ph.D. in Engineering',
            'Ph.D. in Literature',
            'Others'
        ]
    }
    if request.method == 'POST':
        # Get form inputs
        education = request.POST.get('education')
        selected_course = request.POST.get('selected_course')
        job = request.POST.get('job')
        worked_at = request.POST.get('worked_at')
        religion = request.POST.get('religion')
        caste = request.POST.get('caste')
        district = request.POST.get('district')
        place = request.POST.get('place')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        age = request.POST.get('age')
        mob = request.POST.get('mob')
        marital_status = request.POST.get('marital_status')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        about = request.POST.get('about')
        email = request.POST.get('email')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        male_siblings = request.POST.get('male_siblings')
        female_siblings = request.POST.get('female_siblings')
        married_male_siblings = request.POST.get('married_male_siblings')
        married_female_siblings = request.POST.get('married_female_siblings')



        # Update fields only if they have new data
        if education:
            user_profile.education = education
        if email:
            request.user.email = email
            request.user.save()

        if selected_course:
            user_profile.selected_course = selected_course
        if job:
            user_profile.job = job
        if worked_at:
            user_profile.worked_at = worked_at
        if religion:
            user_profile.religion = religion
        if caste:
            user_profile.caste = caste
        if district:
            user_profile.district = district
        if place:
            user_profile.place = place
        if date_of_birth:
            user_profile.date_of_birth = date_of_birth
        if address:
            user_profile.address = address
        if gender:
            user_profile.gender = gender
        if height:
            user_profile.height = height
        if age:
            user_profile.age = age
        if mob:
            user_profile.mob = mob
        if marital_status:
            user_profile.marital_status = marital_status
        if mother_name:
            user_profile.mother_name = mother_name
        if father_name:
            user_profile.father_name = father_name
        if about:
            user_profile.about = about
        if mother_name:
            user_profile.mother_name = mother_name
        if father_name:
            user_profile.father_name = father_name
        if father_job:
            user_profile.father_job = father_job
        if mother_job:
            user_profile.mother_job = mother_job

        if male_siblings:
            user_profile.male_siblings = male_siblings
        if female_siblings:
            user_profile.female_siblings = female_siblings
        if married_male_siblings:
            user_profile.married_male_siblings = married_male_siblings
        if married_female_siblings:
            user_profile.married_female_siblings = married_female_siblings

        # Only update profile picture if it's provided in the request
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            user_profile.profile_picture = profile_picture

        # Update photos only if provided in the request
        for i in range(1, 5):
            photo_field_name = f'photo_{i}'
            photo = request.FILES.get(photo_field_name)
            if photo:
                setattr(user_profile, photo_field_name, photo)

        user_profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('view_profile')

    context = {
        'user_profile': user_profile,
        'education_choices': education_choices,
        'course_choices': course_choices,  # Pass course_choices to the template
    }    
    return render(request, 'user/edit_profile.html', context)




from django.shortcuts import render, redirect
from .models import UserProfile

def edit_photos(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_photo_urls = {
        'photo_1': user_profile.photo_1.url if user_profile.photo_1 else None,
        'photo_2': user_profile.photo_2.url if user_profile.photo_2 else None,
        'photo_3': user_profile.photo_3.url if user_profile.photo_3 else None,
        'photo_4': user_profile.photo_4.url if user_profile.photo_4 else None,
    }
    context = {'user_profile': user_profile, 'user_photo_urls': user_photo_urls}
    return render(request, 'user/edit_photos.html', context)

from django.shortcuts import redirect, get_object_or_404
from .models import UserProfile

# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile


def approve_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user_id=user_id)
    
    if not profile.is_approved:
        profile.is_approved = True
        profile.save()
        
        subject = 'Your Matrimony Profile Approval'
        custom_user_id = profile.custom_user_id  
        message_text = f'Your Matrimony profile with custom user ID {custom_user_id} has been approved by the admin. You can now log in.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [profile.user.email]
        send_mail(subject, message_text, from_email, recipient_list, fail_silently=False)
        
        messages.success(request, 'Profile Approved')

    return redirect('user_profiles')  

def reject_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user_id=user_id)
    profile.delete()
    return redirect('user_profiles')  # Redirect to your user profiles admin view

from datetime import timedelta
from datetime import timedelta
from django.utils import timezone

from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import SubscriptionPlan


def create_payment(request):
    plans = [
        {'value': '1_month', 'label': '1 Month - 99.00', 'duration': timezone.timedelta(days=30)},
        {'value': '3_months', 'label': '3 Months - 499.00', 'duration': timezone.timedelta(days=90)},
        {'value': '6_months', 'label': '6 Months - 799.00', 'duration': timezone.timedelta(days=180)},
        {'value': '1_year', 'label': '1 Year - 999.00', 'duration': timezone.timedelta(days=365)},
        {'value': '1_day', 'label': '1 Day - 19.00', 'duration': timezone.timedelta(days=1)},
    ]

    user_profile = request.user.userprofile if request.user.is_authenticated else None

    active_subscription = None
    if user_profile:
        active_subscription = SubscriptionPlan.objects.filter(
            user=user_profile,
            expiration_date__gte=timezone.now()
        ).first()

    if request.method == 'POST':
        selected_plan_value = request.POST.get('plan')
        selected_plan = next((plan for plan in plans if plan['value'] == selected_plan_value), None)

        if selected_plan and user_profile:
            # Check if the user has an active subscription
            if active_subscription:
                messages.error(request, 'You already have an active subscription plan.')
            else:
                expiration_date = timezone.now() + selected_plan['duration']

                SubscriptionPlan.objects.create(
                    user=user_profile,
                    name=selected_plan['label'],
                    amount=selected_plan['label'].split(' - ')[-1].replace('$', ''),
                    payment_date=timezone.now(),
                    expiration_date=expiration_date,
                )

                messages.success(request, 'Payment created successfully.')
        else:
            messages.error(request, 'Selected plan does not exist or user is not authenticated.')

        return redirect('user_home')

    context = {
        'plans': plans,
        'active_subscription': active_subscription,
    }

    return render(request, 'user/user_home.html', context)



def search(request):
    education_options = UserProfile.EDUCATION_CHOICES

    context = {
        'education_options': education_options,
    }

    return render(request, 'user/search.html', context)



from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import UserProfile, SubscriptionPlan
from django.shortcuts import render, redirect

@login_required
def search_results(request):
    user_profile = request.user.userprofile
    active_subscription = SubscriptionPlan.objects.filter(
        user=user_profile,
        expiration_date__gte=timezone.now()
    ).first()

    # If the user doesn't have an active subscription or it has expired, restrict access
    if not active_subscription:
        messages.error(request, "You do not have an active subscription. Please subscribe to access this feature.")
        return render(request, 'user/error.html')

    # Determine the opposite gender
    user_gender = user_profile.gender
    opposite_gender = 'female' if user_gender == 'male' else 'male'

    education_options = UserProfile.EDUCATION_CHOICES
    religion_options = UserProfile.RELIGION_CHOICES
    districts = UserProfile.objects.values_list('district', flat=True).distinct()

    query = request.GET.get('q')
    education = request.GET.get('education')
    religion = request.GET.get('religion')
    age_range = request.GET.get('age_range')
    district = request.GET.get('district')

    # Filter results by opposite gender
    results = UserProfile.objects.filter(gender=opposite_gender)

    if query:
        results = results.filter(some_field__icontains=query)
    if education:
        results = results.filter(education=education)
    if religion:
        results = results.filter(religion=religion)
    if age_range:
        age_start, age_end = map(int, age_range.split('-'))
        results = results.filter(age__gte=age_start, age__lte=age_end)
    if district:
        results = results.filter(district=district)

    context = {
        'results': results,
        'education_options': education_options,
        'religion_options': religion_options,
        'districts': districts,
        'selected_education': education,
        'selected_religion': religion,
        'selected_age_range': age_range,
        'selected_district': district,
    }

    return render(request, 'user/search_results.html', context)


from django.shortcuts import render
from .models import UserProfile  # Import the UserProfile model
from django.db.models import Q  # Import for complex queries

from django.db.models import Q

def search_id(request):
    user_profile = request.user.userprofile
    active_subscription = SubscriptionPlan.objects.filter(
        user=user_profile,
        expiration_date__gte=timezone.now()
    ).first()

    # If the user doesn't have an active subscription or it has expired, restrict access
    if not active_subscription:
        messages.error(request, "You do not have an active subscription. Please subscribe to access this feature.")
        return render(request, 'user/error.html')
    
    user_gender = user_profile.gender
    opposite_gender = 'female' if user_gender == 'male' else 'male'

    query = request.GET.get('q')  # Get the search query from the URL parameter
    
    if query:
        results = UserProfile.objects.filter(
            Q(custom_user_id__icontains=query) &
            Q(gender=opposite_gender)  # Filter by opposite gender
        )
    else:
        results = UserProfile.objects.filter(gender=opposite_gender)
    
    context = {
        'results': results,
        'query': query,
    }
    
    return render(request, 'user/search_results_id.html', context)



def search_id_admin(request):
    query = request.GET.get('q')  
    
    if query:
        results = UserProfile.objects.filter(Q(custom_user_id__icontains=query))
    else:
        results = UserProfile.objects.all()
    
    context = {
        'results': results,
        'query': query,
    }
    
    return render(request, 'admin/search_id.html', context)



def report_user(request, user_id):
    user_to_report = UserProfile.objects.get(id=user_id)

    if request.method == 'POST':
        reason = request.POST['reason']
        description = request.POST['description']
        
        report = Report.objects.create(
            user=request.user.userprofile,
            reported_user=user_to_report,
            reason=reason,
            description=description
        )
        
        messages.success(request, 'User reported successfully.')
        return redirect('all_users')  # Redirect to the all_users view
    
    context = {
        'user_to_report': user_to_report,
    }
    return render(request, 'user/all_users.html', context)



def view_report_profile(request):
    # Get the user profile of the currently logged-in user
    user_profile = UserProfile.objects.get(user=request.user)

    # Retrieve all reports made by the current user
    reports = Report.objects.filter(user=user_profile)

    education_choices = UserProfile.EDUCATION_CHOICES
    district_choices = UserProfile.objects.values_list('district', flat=True).distinct()
    age_range_choices = [
        ('20-25', '20 to 25'),
        ('25-30', '25 to 30'),
        ('30-35', '30 to 35'),
    ]
    religion_choices = UserProfile.RELIGION_CHOICES

    context = {
        'user_profile': user_profile,
        'reports': reports,
        'education_choices': education_choices,
        'district_choices': district_choices,
        'age_range_choices': age_range_choices,
        'religion_choices': religion_choices,
    }

    return render(request, 'user/view_report_profile.html', context)


from django.shortcuts import render
from .models import Report

def all_reports(request):
    # Retrieve all reports
    reports = Report.objects.all()

    context = {
        'reports': reports,
    }

    return render(request, 'admin/all_reports.html', context)


from django.shortcuts import render
from .models import UserProfile, SubscriptionPlan
from django.utils import timezone

from django.shortcuts import render
from .models import UserProfile

def all_users(request):
    education_choices = UserProfile.EDUCATION_CHOICES
    district_choices = UserProfile.objects.values_list('district', flat=True).distinct()
    age_range_choices = [
        ('20-25', '20 to 25'),
        ('25-30', '25 to 30'),
        ('30-35', '30 to 35'),
    ]    
    religion_choices = UserProfile.RELIGION_CHOICES

    # Filter profiles by gender and approval status
    opposite_gender = 'male' if request.user.is_authenticated and request.user.userprofile.gender == 'female' else 'female'
    opposite_gender_profiles = UserProfile.objects.filter(gender=opposite_gender, is_approved=True)
    
    user_has_active_subscription = False
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        active_subscription = SubscriptionPlan.objects.filter(
            user=user_profile,
            expiration_date__gte=timezone.now()
        ).first()
        if active_subscription:
            user_has_active_subscription = True

    context = {
        'opposite_gender_profiles': opposite_gender_profiles,
        'user_has_active_subscription': user_has_active_subscription,
        'education_choices': education_choices,
        'district_choices': district_choices,
        'age_range_choices': age_range_choices,
        'religion_choices': religion_choices,
    }

    return render(request, 'user/all_users.html', context)


from django.contrib import messages

@login_required
def add_interest(request, profile_id):
    user_profile = request.user.userprofile

    interest_profile = UserProfile.objects.get(id=profile_id)

    Interest.objects.create(user=user_profile, interest_user=interest_profile)

    messages.success(request, f'You have added interest in {interest_profile.user.username}.')
    
    return redirect('interested_profiles')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Interest

@login_required
def interested_profiles(request):
    user_profile = request.user.userprofile

    # Fetch the list of profiles that the user has expressed interest in
    interested_profiles = Interest.objects.filter(user=user_profile).values_list('interest_user', flat=True)

    # Get the actual user profiles using the IDs obtained from interests
    profiles = UserProfile.objects.filter(id__in=interested_profiles)
    district_choices = UserProfile.objects.values_list('district', flat=True).distinct()
    
    # Fetch other available choices (education, religion, and age range)
    education_choices = UserProfile.EDUCATION_CHOICES
    religion_choices = UserProfile.RELIGION_CHOICES
    age_range_choices = [
        ('20-25', '20 to 25'),
        ('25-30', '25 to 30'),
        ('30-35', '30 to 35'),
        # Add more age range choices as needed
    ]

    context = {
        'profiles': profiles,
        'education_choices': education_choices,
        'district_choices': district_choices,
        'age_range_choices': age_range_choices,
        'religion_choices': religion_choices,

    }

    return render(request, 'user/interested_profiles.html', context)

@login_required
def remove_interest(request, profile_id):
    user_profile = request.user.userprofile

    interest_profile = UserProfile.objects.get(id=profile_id)

    try:
        interest = Interest.objects.get(user=user_profile, interest_user=interest_profile)
        interest.delete()
    except Interest.DoesNotExist:
        pass

    return redirect('intereseted_profiles') 




@login_required
def subscription_list(request):
    user_profile = request.user.userprofile  # Access the user profile associated with the user
    subscriptions = SubscriptionPlan.objects.filter(user=user_profile)
    return render(request, 'user/subscription_list.html', {'subscriptions': subscriptions})



@login_required
def subscription_list_admin(request):
    subscriptions = SubscriptionPlan.objects.all()
    return render(request, 'admin/subscription_list_admin.html', {'subscriptions': subscriptions})




from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Retrieve the new password from the form before saving it
            new_password = form.cleaned_data['new_password1']

            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')

            # Send an email to the user with the updated password
            subject = 'Your Updated Password'
            message_text = f'Your new password is: {new_password}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message_text, from_email, recipient_list, fail_silently=False)

            return redirect('login_view')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
            return redirect('change_password')  # Redirect back to the password change page with error messages.
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from django.contrib.auth.models import User

@login_required
def send_message(request, receiver_username):
    receiver = get_object_or_404(User, username=receiver_username)

    if request.method == 'POST':
        content = request.POST.get('message_content')
        if content:
            message = Message(sender=request.user, receiver=receiver, content=content)
            message.save()
            messages.success(request, 'Message sent successfully.')
        else:
            messages.error(request, 'Message content cannot be empty.')

    return redirect('all_users')

# views.py

@login_required
def show_messages(request, receiver_username):
    receiver = get_object_or_404(User, username=receiver_username)

    # Get the received messages
    received_messages = Message.objects.filter(sender=receiver, receiver=request.user).order_by('timestamp')

    # Get the sent messages
    sent_messages = Message.objects.filter(sender=request.user, receiver=receiver).order_by('timestamp')

    context = {
        'receiver': receiver,
        'received_messages': received_messages,
        'sent_messages': sent_messages,
    }
    return render(request, 'user/show_messages.html', context)
