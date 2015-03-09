# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserUpdateForm

# Import the customized User model
from .models import User

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    # These next two lines tell the view to index lookups by email
    slug_field = "email"
    slug_url_kwarg = "email"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"email": self.request.user.email})

class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by email
    slug_field = "email"
    slug_url_kwarg = "email"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    # we already imported User in the view code above, remember?
    model = User
    form_class = UserUpdateForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"email": self.request.user.email})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(email=self.request.user.email)
