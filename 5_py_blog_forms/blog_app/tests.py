

# Create your tests here.


from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):


 def setUp(self):


    self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
    ) 
    self.post = Post.objects.create(
        titulo='A good titulo',
        texto='Nice texto content',
        autor=self.user,
    )
 def test_string_representation(self):
    post = Post(titulo='A sample titulo')
    self.assertEqual(str(post), post.titulo)


 def test_get_absolute_url(self):


    self.assertEqual(self.post.get_absolute_url(), '/')


 def test_post_content(self):


    self.assertEqual(f'{self.post.titulo}', 'A good titulo')
    self.assertEqual(f'{self.post.autor}', 'testuser')
    self.assertEqual(f'{self.post.texto}', 'Nice texto content')


 def test_post_list_view(self):


    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice texto content')
    self.assertTemplateUsed(response, 'home.html')


 def test_post_detail_view(self):


    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/100000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'A good titulo')
    self.assertTemplateUsed(response, 'post_detalle.html')


 def test_post_create_view(self):


    response = self.client.post(reverse('postnuevo'), {
        'titulo': 'New titulo',
        'texto': 'New text',
        'autor': self.user,
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'New titulo')
    self.assertContains(response, 'New text')


 def test_post_update_view(self):


    response = self.client.post(reverse('postedit', args='1'), {
        'titulo': 'Updated titulo',
        'texto': 'Updated text',
    })
    self.assertEqual(response.status_code, 302)


 def test_post_delete_view(self):


    response = self.client.get(
        reverse('postdelete', args='1'))
    self.assertEqual(response.status_code, 200)
