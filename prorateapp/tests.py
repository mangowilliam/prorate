from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestclass(TestCase):
    def setUp(self):
        self.mango= Profile(bio = "imagine the world at your disposal", email ='juniormangoyahoo.com',phone_number="0702658317")
    def test_instance(self):
        self.assertTrue(isinstance(self.mango,Profile))
    
    def tearDown(self):
        Profile.objects.all().delete
    
    def test_save(self):
        self.mango.save_editor()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete(self):
        self.mango.save()
        self.mango.delete()
        self.assertTrue(len(Location.objects.all())== 0)
        
    def test_update(self):
        self.mango>save()
        self.mango.username="mangoes"
        self.assertTrue(self.mango.username == 'mangoes')
        
        
        
class ProjectTestclass(TestCase):
    def setUp(self):
        self.mango=Profile(username = 'mango')
        self.mango.save_profile()
        
        self.new_project = Project(title = "delani", description ='landing page')
        self.new_project.save()
        
    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        
    def test_instance(self):
        self.delani.save()
        self.assertTrue(isinstance(self.delani,Project))
    
    def test_delete(self):
        self.delani.save()
        self.delani.delete()
        self.assertTrue(len(Project.objects.all())==0)
    
    def test_update(self):
        self.delani.save()
        self.delani.title = "studio"
        self.assertTrue(self.delani.title == "studio")
    def test_search_project(self):
        self.delani.save()
        projects =Project.search_project(self.delani)
        self.assertTrue(len(images) > 0)