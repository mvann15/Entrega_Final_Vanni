from django.urls import path
from accounts.views import login_request, logout_request, register_request, editar_request, editar_avatar_request

urlpatterns = [

    path('login/', login_request, name="Login"),
    path('logout/', logout_request, name="Logout"),
    path('registro/', register_request, name="Registro"),
    path('editar/', editar_request, name="Editar"),
    path('avatar/', editar_avatar_request, name="Avatar"),

]
