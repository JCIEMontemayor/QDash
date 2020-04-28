from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, postdata):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['f_name']) < 4 or len(postdata['l_name']) < 4:
            errors['name'] = "Your NAME is not good enough"

        if not email_checker.match(postdata['email']):
            errors['email'] = "Enter a valid email address"

        if len(postdata['pass']) < 4:
            errors['pass'] = "Your PASSWORD could use a few more CHARACTERS"

        if postdata['pass'] != postdata['con_pass']:
            errors['pass'] = "Your PASSWORD does NOT match, PLEASE try again."

        return errors

class QuoteManager(models.Manager):
    def quote_validator(self, postdata):
        errors = {}
        if len(postdata['q_desc']) < 10:
            errors['q_desc'] = "You need more WORDS!"

        if len(postdata['q_auth']) < 3:
            errors['q_auth'] = "Not a REAL user"

        return errors

class LoginManager(models.Manager):
    def login_validator(self, postdata):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_checker.match(postdata['email']):
            errors['email'] = "Enter a valid email address"
        if len(postdata['pass']) < 4:
            errors['pass'] = "Your PASSWORD is incorrect"
        return errors

# class EditManager(models.Manager):
#     def edit_validator(self, postdata):
#         errors = {}
#         email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not email_checker.match(postdata['email']):
#             errors['email'] = "Enter a valid email address"
#         if len(postdata['f_name']) < 4 or len(postdata['l_name']) < 4:
#             errors['name'] = "Your NAME is not good enough"
#         return errors

        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='user_quote', on_delete=models.CASCADE)
    objects = QuoteManager()
    user_likes = models.ManyToManyField(User, related_name='liked_quote')

class Login(models.Model):
    logged_email = models.CharField(max_length=255)
    logged_password = models.CharField(max_length=255)
    objects = LoginManager()

# class Edit(models.Model):
#     new_first_name = models.CharField(max_length=255)
#     new_last_name = models.CharField(max_length=255)
#     new_email = models.CharField(max_length=255)
#     objects = EditManager()






# Create your models here.
