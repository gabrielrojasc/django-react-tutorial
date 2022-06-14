# django
from django.urls import path

from .views import CreateRoomView
from .views import RoomView

urlpatterns = [
    path("room/", RoomView.as_view()),
    path("create-room", CreateRoomView.as_view()),
]
