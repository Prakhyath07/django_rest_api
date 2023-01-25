from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    body = request.body # byte string of json
    params = request.GET
    print(params)
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(params)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)