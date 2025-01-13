from django.urls import path
from .views import DoodleView

app_name = 'doodle'

urlpatterns = [
    path('', DoodleView.as_view(), name='doodle_page'),
    path('save/', DoodleView.as_view(), name='save_doodle'),
]