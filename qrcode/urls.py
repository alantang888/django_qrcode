from django.conf.urls import url

from . import views

app_name = 'qrcode'
urlpatterns = [
    url(r'^gen_qrcode/((?P<scale>\d+)/)?(?P<qrcode_data>.+)/$', views.get_qrcode_png,
        name='gen_qrcode_from_url'),
    url(r'^gen_session_qrcode/((?P<scale>\d+)/)?(?P<session_key>[^/]+)/$', views.get_qrcode_png_from_session,
        name='gen_qrcode_from_session'),

    # This is for test gen QR code from session data, normally you can do it in your code.
    # url(r'^test_session_qrcode/$', views.test_session_qrcode),
]