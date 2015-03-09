from django.core.urlresolvers import reverse
from django.test import TestCase


from .models import User

class ModelTestCase(TestCase):

    def test_model_create_admin(self):

        self.admin_user = User.objects.create(email='admin@admin.org',
            password="test", is_superuser=True)
        self.non_admin_user = User.objects.create(email='joe@schmoe.org',
            password="test", is_superuser=False)

        self.assertTrue(self.admin_user.is_superuser)
        self.assertFalse(self.non_admin_user.is_superuser)
