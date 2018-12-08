from django.test import TestCase
from django.urls import reverse

from catalog.models import Person

class PersonListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons for pagination tests
        number_of_persons = 13

        for person_id in range(number_of_persons):
            Person.objects.create(
                first_name=f'Christian {person_id}',
                last_name=f'Surname {person_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/persons/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/person_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('persons'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['person_list']) == 10)

    def test_lists_all_persons(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('persons')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['person_list']) == 3)