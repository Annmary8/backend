from django.urls import path
from api.views import RegisterView,LoginView,SkillListCreateView, SkillRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyView.as_view(), name='skill-detail'),
]
