from django.urls import path
from notes.views import NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    
	path("", NoteListView.as_view(), name="note-list"),
	path("create/", NoteCreateView.as_view(), name="note-create"),
	path("<int:pk>/delail/", NoteDetailView.as_view(), name="note-detail"),
    path("<int:pk>/edit/", NoteUpdateView.as_view(), name="note-edit"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete")
    
]
