from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexPage, name='index'),
    path('signup/',views.signUpPage,name='signup'), 
    path('login/',views.loginPage,name='login'),
    path('home/',views.homePage,name='home'),
    path('quotes/',views.quotesPage,name='quotes'),
    path('prompts/',views.promptsPage,name='prompts'),
    path('stickynotes/',views.stickyNotesList.as_view(),name="stickynotes.list"),
    path ('stickynotes/<int:pk>/',views.stickyNotesDetailView.as_view(),name="stickynotes.detail"),
    path ('stickynotes/<int:pk>/edit/',views.stickyNotesUpdateView.as_view(),name="stickynotes.update"),
    path ('stickynotes/<int:pk>/delete/',views.stickyNotesDeleteView.as_view(),name="stickynotes.delete"),
    path('stickynotes/new/',views.stickyNotesCreateView.as_view(),name="stickynotes.new"),
    path('notes/', views.NotesListView.as_view(), name="notes.list"),
    path('notes/new/',views.NotesCreateView.as_view(),name="notes.new"),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit/', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete/', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('tinymce/', include('tinymce.urls')), #for using tinymce editor
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 


   

    path('timetable/', views.timetable, name='timetable'),
    path('add_event/', views.add_event, name='add_event'),
    path('todo_home/', views.index, name='todo_home'),  # Main Todo List page
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('reminder_view/', views.reminder_view, name='reminder_view'),
    path('add/', views.add_reminder, name='add_reminder'),
    path('delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
    path('books/', views.book_view, name='book_view'),  # New book view
    path('upload/', views.upload_book, name='upload_book'),
    path('books/', views.get_books, name='get_books'),
    path('search/', views.search_books, name='search_books'),

    
]
