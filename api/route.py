from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.quiz.views import (
    CategoryListView,
    StartQuizApiView
)

from api.auth.views import (
    UserRegisterView,
    UserAuthenticateView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [

        # Registration
        path("user-register/", UserRegisterView.as_view(), name="user-register"),
        # path("manager-register/", ManagerRegisterView.as_view(), name="manager-register"),

        # Login
        path("user-login/", UserAuthenticateView.as_view({"post": "login"}), name="login"),
        path("user-logout/", UserAuthenticateView.as_view({"post": "logout"}), name="logout"),

        # Quiz
        path("category-list/", CategoryListView.as_view(), name="category-list"),
        path("submit-test/<int:pk>/", StartQuizApiView.as_view(), name="category-list"),
    ]
)
