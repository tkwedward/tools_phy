from django.conf.urls import url
from .views import upload, result

urlpatterns = [
    url('upload', upload, name="upload"),
    url('result', result, name="result"),
]
