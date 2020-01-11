from django.urls import path

from static.models import StaticPage
from static.views import StaticPageView

urlpatterns = [
    path('', StaticPageView.as_view(pagetype=StaticPage.PageType.Top)),
]