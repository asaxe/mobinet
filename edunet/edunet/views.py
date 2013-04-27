from django.http import HttpResponse

def home(request):
    output = '<br> '.join([ header + ": " + str(value) for (header, value) in request.META.items()])
    return HttpResponse(output)
