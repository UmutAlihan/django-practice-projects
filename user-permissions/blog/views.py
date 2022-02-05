from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new

from .models import Post

# Generally permissions are set in the views.py file.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


# (1) we want a user to be logged in before they can access BlogUpdateView
# the simplest, in my opinion, is to use the built in LoginRequiredMixin.
# a mixin called in order from left to right so we'll want to add the login mixin before UpdateView.
# f a user is not logged in, they'll see an error message.
# (2) next-level permissions is something specific to the user
# to enforce the rule that only the author of a blog post can update it
# use the built-in UserPassesTestMixin for this.
# (3) a user must first be logged in and then they must pass the user test before accessing UpdateView
# generally it's better to start with the most general permissions and then become more granular as you move along to the right
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        # test_func method is used by UserPassesTestMixin for our logic. We need to override it.
        # In this case we set the variable obj to the current object returned by the view using get_object.
        obj = self.get_object()
        # if the author on the current object matches the current user on the webpage, then allow it
        return obj.author == self.request.user
# There are other ways to set per-user permissions including overriding the dispatch method


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
