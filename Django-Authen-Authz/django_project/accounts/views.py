from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth import login


# (Class registry) registry using a built-in class ----
"""
# from django.urls import reverse_lazy
# from django.views import generic

    class RegisterView(generic.CreateView):
        form_class = CreateUserForm
        template_name = 'registry.html'
        success_url = reverse_lazy('weblog:index')
"""
# -----------------------------------------------------

# (function registry) ---------------------------------
def registry(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('weblog:index') 
        return render(request, 'registry.html', {'form': form})

    else:
        form = CreateUserForm()
        return render(request, 'registry.html', {'form': form})
# ------------------------------------------------------
            