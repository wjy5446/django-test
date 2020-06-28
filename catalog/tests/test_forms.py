import datetime

from django.test import TestCase
from django.utils import timezone

from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['due_back'].label == None or form.fields['due_back'].label == 'renewal date')

    def test_renew_form_date_filed_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['due_back'].help_text, 'Enter a date between now and 4 weeks (default 3).')

    def test_renew_form_date_in_past(self):
        data = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'due_back': data})
        self.assertFalse(form.is_valid())
    
    def test_renew_form_date_too_far_in_future(self):
        data = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'due_back': data})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        data = datetime.date.today()
        form = RenewBookForm(data={'due_back': data})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        data = timezone.now() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'due_back': data})
        self.assertTrue(form.is_valid())