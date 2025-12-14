from django.http import HttpResponse


def index_view(request):
    html = f"""
        <html><body>
        <p>Główny widok</p>
        </body></html>"""
    return HttpResponse(html)