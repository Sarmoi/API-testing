import requests
from django.shortcuts import render

def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']
  return render(request, 'templates/index.html', {'fact': fact})
