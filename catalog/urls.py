from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('educations/', views.EducationListView.as_view(), name='educations'),
    path('education/<int:pk>', views.EducationDetailView.as_view(), name='education-detail'),
]

urlpatterns += [   
    path('mypersons/', views.CreatedByUserListView.as_view(), name='my-person'),
]

urlpatterns += [  
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]

urlpatterns += [  
    path('location/create/', views.LocationCreate.as_view(), name='location_create'),
    path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
]

urlpatterns += [  
    path('education/create/', views.EducationCreate.as_view(), name='education_create'),
    path('education/<int:pk>/update/', views.EducationUpdate.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', views.EducationDelete.as_view(), name='education_delete'),
]