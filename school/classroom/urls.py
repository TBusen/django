from django.urls import path

# from .views import home_view
from .views import HomeView, ThankYou, ContactFormView

app_name = "classroom"

urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
]
