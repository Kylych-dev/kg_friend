from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.quiz.views import (
    CategoryListView,
    # SubmitAnswerView
    StartQuizApiView
)

# from .v1.cart.views import (
#     CartModelViewSet,
# )

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

        # path("category-list/", CategoryListView.as_view({"get": "products_list"}), name="products-list"),
        # path("products-detail/<slug:slug>/", ProductModelViewSet.as_view({"get": "product_detail"}), name="products-detail"),

        # # Cart
        # path("cart-list/", CartModelViewSet.as_view({"get": "cart_list"}), name="cart"),
        # path("cart-add/", CartModelViewSet.as_view({"post": "cart_add"}), name="cart-add"),
        # path("cart-update/", CartModelViewSet.as_view({"post": "cart_update"}), name="cart-update"),
        # path("cart-delete/", CartModelViewSet.as_view({"post": "cart_delete"}), name="cart-delete"),
        #
        # # Category
        # path("category-list/<slug>/", CategoryModelViewSet.as_view({"get": "category_list"}), name="category-list"),


        # Payment
        # path("shipping/", .as_view({"post": "create"}), name="shipping"),
        # path("checkout/", .as_view({"post": "create"}), name="checkout"),
        # path("complete-order/", .as_view({"post": "create"}), name="complete-order"),
        # path("payment-success/", .as_view({"post": "create"}), name="payment-success"),
        # path("payment-fail/", .as_view({"post": "create"}), name="payment-fail"),



        # path("apartments/create/", EstablishmentModelViewSet.as_view({"post": "create"}), name="apartments-create"),
        # path("apartments/update/<int:pk>/", EstablishmentModelViewSet.as_view({"put": "update"}),
        #      name="apartments-update"),
        # path("apartments/delete/<int:pk>/", EstablishmentModelViewSet.as_view({"delete": "delete"}),
        #      name="apartments-delete"),


    ]
)
