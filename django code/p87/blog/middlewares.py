from django.shortcuts import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        print("This is Process View ")
        # return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("This is Process View ")
        # return HttpResponse("This is before view")
        return HttpResponse(exception)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process template response from middleware")
        response.context_data['name'] = 'basant'
        return response
