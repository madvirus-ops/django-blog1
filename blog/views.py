from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from froala_editor.widgets import FroalaEditor

#def home(request):
#	context = {'posts':Posts.objects.all()}
#	return render(request,'blog/home.html',context)

class PostListView(ListView):
	model = Posts 
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6


class UserPostListView(ListView):
	model = Posts 
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	paginate_by = 8

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Posts.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Posts 


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Posts 
	fields = ['title','content','image']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
	model = Posts 
	fields = ['title','content','image']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

	def test_func(self):
		posts= self.get_object()
		if self.request.user == posts.author:
			return True
		return False


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
	model = Posts 
	success_url = '/'
	def test_func(self):
		posts= self.get_object()
		if self.request.user == posts.author:
			return True
		return False


def about(request):
	return render(request,'blog/about.html')

