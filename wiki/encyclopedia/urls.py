from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.EntryListView.as_view(), name="index"),
    path("entries/",views.EntryListView.as_view(),name='entries'),
    path("entry/<int:pk>",views.EntryDetailView.as_view(),name="entry_detail"),
    path("<int:pk>", views.EntryDetailView.as_view(), name="path_entry-detail"),
    path("<slug:subject>",views.get_obj_orlist, name="entry-bysubject"),
    path("random/",views.randompage,name="randompage"),
    path("searchwiki/",views.searchwiki,name="searchwiki"),
]

# Add URLConf to create, update, and delete wiki entries
urlpatterns += [
    path('entry/create/', views.EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/update/', views.EntryUpdateView.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
]

# wildcard url for everything else
urlpatterns += [
    re_path(r'^.*', views.urlguidance),
]
