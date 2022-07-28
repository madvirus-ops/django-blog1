 from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from blog.forms import Postsform
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
#remove this block later
@login_required
def Postnew(request):
    if request.method == 'POST':
        form = Postsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'post created ')
            return redirect('post-detail')
    else:
        form = Postsform()
    context ={
        'form':form,
    }
    return render(request,'blog/post2form.html',context)
	
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

