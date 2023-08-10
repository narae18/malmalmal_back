# from django.db import models

# from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ID = models.CharField(max_length=20)
#     nickname = models.CharField(max_length=10)
#     birthday = models.DateField()
#     address = models.CharField(max_length=100)  

#     def __str__(self):
#         return self.user.username


# class EditorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ID = models.CharField(max_length=20)
#     name = models.CharField(max_length=10)
#     address = models.CharField(max_length=100)  

#     def __str__(self):
#         return self.user.username