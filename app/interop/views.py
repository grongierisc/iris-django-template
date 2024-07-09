from django.http import HttpResponse

from iop import Director

bs = Director.create_python_business_service('BS')

def index(request):
    result = bs.on_process_input(request)
    return HttpResponse(result)
