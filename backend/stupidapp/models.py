from django.db import models


BLOOD_GROUPS = [
    ("A-", "A-"),
    ("A+", "A+"),
    ("B-", "B-"),
    ("B+", "B+"),
    ("AB-", "AB-"),
    ("AB+", "AB+"),
    ("O-", "O-"),
    ("O+", "O+"),
]

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

COMPLICATIONS = [
    ("Still Birth", "Still Birth"),
    ("Live Birth", "Live Birth"),
    ("Abortion", "Abortion"),
]

EDUCATIONS = [
    ("Illiterate", "Illiterate"),
    ("Primary School", "Primary School"),
    ("Middle School", "Middle School"),
    ("High School", "High School"),
    ("Graduate", "Graduate"),
]


class Mother(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    rch_id = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    mobile = models.CharField(max_length=10, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    blood_group = models.CharField(max_length=255, null=False, blank=False, choices=BLOOD_GROUPS)
    delivery_complication = models.CharField(max_length=255, null=False, blank=False, choices=COMPLICATIONS)
    education = models.CharField(max_length=255, null=False, blank=False, choices=EDUCATIONS)


class Child(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    blood_group = models.CharField(max_length=255, null=False, blank=False, choices=BLOOD_GROUPS)
    gender = models.CharField(max_length=255, null=False, blank=False, choices=GENDERS)


class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Campaign(models.Model):
    organizer = models.ForeignKey("Organization", null=False, blank=False, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, blank=False)    
    end_date = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)


class Course(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Vaccine(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    course = models.ForeignKey("Course", null=False, blank=False, on_delete=models.CASCADE)
    sequence = models.IntegerField(null=False, blank=False)


class Immunization(models.Model):
    child = models.ForeignKey("Child", null=False, blank=False, on_delete=models.CASCADE)
    date_of_vaccination = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    vaccine = models.ForeignKey("Vaccine", null=False, blank=False, on_delete=models.CASCADE)
    campaign = models.ForeignKey("Campaign", null=False, blank=False, on_delete=models.CASCADE)
