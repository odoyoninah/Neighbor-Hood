from django.test import TestCase
from .models import *

# Create your tests here.
class HoodTest(TestCase):
    def setUp(self):
        self.hood = Hood(name='Kampala', location='Nairobi', occupants=100)
        self.hood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))

    def test_save_hood(self):
        self.hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):
        self.hood.delete_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 0)

    def test_update_hood(self):
        self.hood.update_hood(name='Kampala', location='Nairobi', occupants=100)
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)

class BusinessTest(TestCase):
    def setUp(self):
        self.business = Business(name='Kampala', location='Nairobi', occupants=100)
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_update_business(self):
        self.business.update_business(name='Kampala', location='Nairobi', occupants=100)
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

# class ProfileTest(TestCase):
#     def setUp(self):
#         self.profile = Profile(name='Kampala', location='Nairobi', occupants=100)
#         self.profile.save()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile, Profile))

#     def test_save_profile(self):
#         self.profile.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)

#     def test_delete_profile(self):
#         self.profile.delete_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) == 0)

#     def test_update_profile(self):
#         self.profile.update_profile(name='Kampala', location='Nairobi', occupants=100)
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)

class PostTest(TestCase):
    def setUp(self):
        self.post = Post(name='Kampala', location='Nairobi', occupants=100)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

    def test_update_post(self):
        self.post.update_post(name='Kampala', location='Nairobi', occupants=100)
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
