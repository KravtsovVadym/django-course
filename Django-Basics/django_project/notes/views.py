from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from notes.models import Note 
from notes.forms import NoteForm

class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"


class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"


class NoteCreateView(CreateView):
    template_name = "notes/note_create.html"
    form_class = NoteForm
    success_url = reverse_lazy("note-list")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_edit.html"
    success_url = reverse_lazy("note-list")

class NoteDeleteView(DeleteView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_delete.html"
    success_url = reverse_lazy("note-list")
