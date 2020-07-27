from django.urls import path
from core.views import SignUpView, ProfileView,image_upload_view
from.import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('upload/', views.image_upload_view)
]