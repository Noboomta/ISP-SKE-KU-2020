from django.test import TestCase
from django.urls import reverse

from .models import Todo

class TodoTests(TestCase):

    def test_if_todo_in_index(self):
        """ test if todo which is created is already in index page. """
        todo = Todo.objects.create(description="be a good man", done=False)
        url = reverse('todo:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, todo.description)

    def test_if_no_todo_in_index(self):
        """ test if no todo which already done. """
        todo = Todo.objects.create(description="be a good son", done=False)
        reverse("todo:done", args = (todo.id,))
        response = self.client.get(reverse('todo:index'))
        self.assertContains(response, todo.description)

    def test_if_redirect_to_index(self):
        """ test if the response after done  atodo is index page. """
        todo = Todo.objects.create(description="be a good student", done=False)
        url = reverse('todo:done', args=(todo.id,))
        response = self.client.get(url)
        self.assertRedirects(response, reverse("todo:index"))
        # self.assertEqual(response.status_code, 302)

    def test_if_404_after_wrong_id(self):
        """ test if the 404 status code returned after sent an fake id to the done page. """
        todo = Todo.objects.create(description="be a good student", done=False)
        fake_id = 3
        url = reverse('todo:done', args=(fake_id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

