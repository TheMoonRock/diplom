from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello", headers={"SecretCode": "21234567"})
