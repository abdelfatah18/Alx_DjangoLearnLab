from rest_framework.authtoken.views import obtain_auth_token  # ✅ Import obtain_auth_token
from django.urls import path

urlpatterns = [
    # Route to obtain the token
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # ✅ Token retrieval endpoint
    ...
]
