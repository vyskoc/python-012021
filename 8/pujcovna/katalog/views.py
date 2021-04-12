from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
        <a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>
        <h2>O naší autopůjčovně</h2>
        <p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
        """)

class SeznamView(View):
    def get(self, request):
        return HttpResponse("""<h4>Seznam aut:</h4>
        <ol type="a">
  <li>Škoda</li>
  <li>Renault</li>
  <li>Ford</li>
</ol>""")