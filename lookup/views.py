# this is my view.py file 
from django.shortcuts import render

def home(request):
	import json
	import requests 
	
	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=66681BC7-E6FD-4B3F-99BF-1753ABEA4121")
	
	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error... unable to connet at the moment"

	return render(request, 'home.html', {'api': api})	

def about(request):
	return render(request, 'about.html', {})
