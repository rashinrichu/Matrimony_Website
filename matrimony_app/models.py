from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    RELIGION_CHOICES = [
        ('hindu', 'Hindu'),
        ('muslim', 'Muslim'),
        ('christian', 'Christian'),
        ('sikh', 'Sikh'),  
        ('unspecified', 'unspecified'),

    ]
    
    CASTE_CHOICES = [
    ('brahmin', 'Brahmin'),
    ('kshatriya', 'Kshatriya'),
    ('vaishya', 'Vaishya'),
    ('shudra', 'Shudra'),
    ('darzi', 'Darzi'),
    ('jolaha', 'Jolaha'),
    ('fakir', 'Fakir'),
    ('rangrez', 'Rangrez'),
    ('unspecified', 'unspecified'),

    # Add more caste choices as needed
]
    DISTRICT_CHOICES = [
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Kollam', 'Kollam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Alappuzha', 'Alappuzha'),
    ('Kottayam', 'Kottayam'),
    ('Idukki', 'Idukki'),
    ('Ernakulam', 'Ernakulam'),
    ('Thrissur', 'Thrissur'),
    ('Palakkad', 'Palakkad'),
    ('Malappuram', 'Malappuram'),
    ('Kozhikode', 'Kozhikode (Calicut)'),
    ('Wayanad', 'Wayanad'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
]
    
    PLACE_CHOICES = [
    ('Thiruvananthapuram', [
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Kovalam', 'Kovalam'),
        ('Neyyattinkara', 'Neyyattinkara'),
        ('Attingal', 'Attingal'),
        ('Varkala', 'Varkala'),
    ]),
    ('Kollam', [
        ('Kollam', 'Kollam'),
        ('Paravur', 'Paravur'),
        ('Punalur', 'Punalur'),
        ('Karunagappally', 'Karunagappally'),
    ]),
    ('Pathanamthitta', [
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Adoor', 'Adoor'),
        ('Thiruvalla', 'Thiruvalla'),
        ('Ranni', 'Ranni'),
    ]),
    ('Alappuzha', [
        ('Alappuzha', 'Alappuzha'),
        ('Chengannur', 'Chengannur'),
        ('Kayamkulam', 'Kayamkulam'),
        ('Haripad', 'Haripad'),
        ('Ambalappuzha', 'Ambalappuzha'),
    ]),
    ('Kottayam', [
        ('Kottayam', 'Kottayam'),
        ('Changanassery', 'Changanassery'),
        ('Palai', 'Palai'),
        ('Vaikom', 'Vaikom'),
    ]),
    ('Idukki', [
        ('Idukki', 'Idukki'),
        ('Thodupuzha', 'Thodupuzha'),
        ('Munnar', 'Munnar'),
        ('Adimali', 'Adimali'),
    ]),
    ('Ernakulam', [
        ('Ernakulam', 'Ernakulam'),
        ('Kochi', 'Kochi'),
        ('Aluva', 'Aluva'),
        ('Paravur', 'Paravur'),
    ]),
    ('Thrissur', [
        ('Thrissur', 'Thrissur'),
        ('Chalakudy', 'Chalakudy'),
        ('Kodungallur', 'Kodungallur'),
        ('Irinjalakuda', 'Irinjalakuda'),
    ]),
    ('Palakkad', [
        ('Palakkad', 'Palakkad'),
        ('Ottapalam', 'Ottapalam'),
        ('Chittur', 'Chittur'),
        ('Mannarkkad', 'Mannarkkad'),
    ]),
    ('Malappuram', [
        ('Malappuram', 'Malappuram'),
        ('Manjeri', 'Manjeri'),
        ('Tirur', 'Tirur'),
        ('Perinthalmanna', 'Perinthalmanna'),
    ]),
    ('Kozhikode', [
        ('Calicut', 'Kozhikode (Calicut)'),
        ('Vadakara', 'Vadakara'),
        ('Thamarassery', 'Thamarassery'),
        ('Ramanattukara', 'Ramanattukara'),
    ]),
    ('Wayanad', [
        ('Wayanad', 'Wayanad'),
        ('Kalpetta', 'Kalpetta'),
        ('Sulthan Bathery', 'Sulthan Bathery'),
        ('Mananthavady', 'Mananthavady'),
    ]),
    ('Kannur', [
        ('Thalassery', 'Thalassery'),
        ('Kannur', 'Kannur'),
        ('Payyannur', 'Payyannur'),
        ('Thaliparamba', 'Thaliparamba'),
        ('Iritty', 'Iritty'),
    ]),
    ('Kasaragod', [
        ('Kasaragod', 'Kasaragod'),
        ('Kanhangad', 'Kanhangad'),
        ('Kumbala', 'Kumbala'),
        ('Cherkala', 'Cherkala'),
    ]),
]

    EDUCATION_CHOICES = [
    ('high_school', 'High School'),
    ('associate_degree', 'Associate Degree'),
    ('bachelors_degree', "Bachelor's Degree"),
    ('masters_degree', "Master's Degree"),
    ('doctorate', 'Doctorate'),
    ('others', 'others'),

]

    MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
]

    SIBLING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    custom_user_id = models.CharField(max_length=10, unique=True, blank=True, null=True)  # Corrected field name    date_of_birth = models.DateField()
    address = models.TextField()
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    selected_course = models.CharField(max_length=20, blank=True, null=True) 
    job = models.CharField(max_length=100)
    worked_at= models.CharField(max_length=100,null=True,blank=True)

    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    caste = models.CharField(max_length=20, choices=CASTE_CHOICES)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    place = models.CharField(max_length=100, choices=PLACE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    photo_1 = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    height = models.CharField(max_length=10)
    age = models.IntegerField()
    mob = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES,null=True,blank=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_job = models.CharField(max_length=100, blank=True, null=True)
    mother_job = models.CharField(max_length=100, blank=True, null=True)  # Field for mother's job
   
    about = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    male_siblings = models.IntegerField(blank=True, null=True)
    female_siblings = models.IntegerField(blank=True, null=True)
    married_male_siblings = models.IntegerField(blank=True, null=True)
    married_female_siblings = models.IntegerField(blank=True, null=True) 
    def __str__(self):
        return self.user.username





class Interest(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interest_user = models.ForeignKey(UserProfile, related_name='interests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user.username} -> {self.interest_user.user.username}'

class Match(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    match_user = models.ForeignKey(UserProfile, related_name='matches', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user.username} matched with {self.match_user.user.username}'



class SubscriptionPlan(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_date = models.DateTimeField(auto_now_add=True, null=True)
    expiration_date = models.DateTimeField(null=True)  # Add this field for expiration date
    def __str__(self):
        return self.name



from django.utils.translation import gettext_lazy as _

class Report(models.Model):
    REASON_CHOICES = [
        ('spam', 'Spam'),
        ('inappropriate_content', 'Inappropriate Content'),
        ('harassment', 'Harassment'),
        ('fake_profile', 'Fake Profile'),
        
    ]
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(UserProfile, related_name='reported_users', on_delete=models.CASCADE)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
    
    def __str__(self):
        return f'{self.user.user.username} reported {self.reported_user.user.username}'



class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} ({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"
