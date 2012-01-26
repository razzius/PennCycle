from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

GRAD_YEAR_CHOICES = (
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('staff', 'staff'),
    ('guest', 'guest'),
    ('grad', 'grad student'),
)

SCHOOL_CHOICES = (
    ('W', 'Wharton'),
    ('E', 'SEAS'),
    ('C', 'College'),
    ('N', 'Nursing'),
    ('O', 'Other'),
)

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    penncard_number = models.CharField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grad_year = models.CharField(max_length=5, choices=GRAD_YEAR_CHOICES)
    join_date = models.DateField(null=True, blank=True)
    height = models.IntegerField(max_length=2)
    school = models.CharField(max_length=10, choices=SCHOOL_CHOICES)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Bike(models.Model):
    bike_name = models.CharField(max_length=100)
    riders = models.ManyToManyField(User, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    purchase_date = models.DateField()
    color = models.CharField(max_length=30, blank=True)
    top_bar = models.CharField(max_length=20, blank=True)
    problems = models.CharField(max_length=300, blank=True)
    #bike_model = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.bike_name

class Ride(models.Model):
    rider = models.ForeignKey(User)
    bike = models.ForeignKey(Bike)
    checkout_time = models.DateTimeField()
    checkin_time = models.DateTimeField(null=True, blank=True)
    ride_duration_days = models.IntegerField()

    def __unicode__(self):
        return u'%s on %s' % (self.rider, self.checkout_time)


