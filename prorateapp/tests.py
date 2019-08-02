from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestclass(TestCase):
    def setUp(self):
        self.mango= Profile(bio = "imagine the world at your disposal", email ='juniormangoyahoo.com',phone_number="0702658317")
    def test_instance(self):
        self.assertTrue(isinstance(self.mango,Profile))
    
    def test_save(self):
        self.mango.save_editor()
        profiles = profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
        
class ProjectTestclass(TestCase):
    def setUp(self):
        self.delani= Project(title = "delani", description ='landing page')
    def test_instance(self):
        self.assertTrue(isinstance(self.delani,Project))
    
    def test_save(self):
        self.delani.save_project()
        projects = projects.objects.all()
        self.assertTrue(len(projects)>0)