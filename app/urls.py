from django.urls import path
from .views import ProjectView, UserCreateView, CourseView, CourseDetailView, ProjectListView, ProjectDetailView, ProjectStartView, ProfileCreateView, LoginView, LogoutView, AccountView, AccountDeleteView, AccountPasswordView

urlpatterns = [
    path('', ProjectView.as_view(), name='top'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>', CourseDetailView.as_view(), name="course"),
    path('project/', ProjectListView.as_view()),
    path('project/(?P<pk>[0-9]+)', ProjectDetailView.as_view(), name="project"),
    path('readyfor/', ProjectStartView.as_view()),
    path('profile/', ProfileCreateView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('account/delete/<int:pk>', AccountDeleteView.as_view(), name='accountDelete'),
    path('account/password/<int:pk>', AccountPasswordView.as_view(), name='accountPassword'),
]
