from django.shortcuts import render, HttpResponse, redirect
import pyqrcode
import io
import numbers
import urllib

# Create your views here.
def gen_qrcode_png_bytes(qrcode_data, scale):
    _scale = scale
    if not isinstance(scale, numbers.Integral):
        try:
            _scale = int(scale)
        except:
            # TODO: raise error for can't parse Int or handle it
            _scale = 5

    qrcode_mem_buffer = io.BytesIO()

    qrcode = pyqrcode.create(qrcode_data)
    qrcode.png(qrcode_mem_buffer, scale=_scale)
    qrcode_bytes = qrcode_mem_buffer.getvalue()
    return qrcode_bytes

def get_qrcode_png(request, qrcode_data, scale=5):
    '''
    This function for generate QR code PNG from URL.
    For security you may don't want the QR code data pass by URL, please consider get_qrcode_png_from_session().
    '''
    _qrcode_data = qrcode_data

    qrcode_bytes = gen_qrcode_png_bytes(_qrcode_data, scale)
    return HttpResponse(qrcode_bytes, content_type='image/png')


def get_qrcode_png_from_session(request, session_key, scale=5):
    '''
    This function for generate QR code PNG from session.
    For security you may don't want the QR code data pass by URL, then you can use this function to pass QR code data by session.
    '''
    if session_key not in request.session:
        # TODO: raise error for no such session
        pass

    qrcode_data = request.session[session_key]

    qrcode_bytes = gen_qrcode_png_bytes(qrcode_data, scale)
    return HttpResponse(qrcode_bytes, content_type='image/png')

def test_session_qrcode(request):
    if request.method == 'POST':
        if 'session_key' in request.POST and 'session_value' in request.POST:
            session_key = request.POST['session_key']
            session_value = request.POST['session_value']
            request.session[session_key] = session_value

            return redirect('qrcode:gen_qrcode_from_session', session_key=session_key)
    return render(request, 'session_test_form.html', locals())