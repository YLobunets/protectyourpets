from django.urls import path

from core.views import PersonListView, PersonCreateView
# from core.views import person_create_view


urlpatterns = [
    path("people/", PersonListView.as_view(), name="person-list"),
    path("people/create/", PersonCreateView.as_view(), name="person-create"),
    # path("people/create/", person_create_view, name="person-create"),
]

app_name = "core"
