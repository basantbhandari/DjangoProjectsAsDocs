class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: FatherMiddleware")

    def __call__(self, request):
        print('This is before view : FatherMiddleware')
        response = self.get_response(request)
        print("This is after view : FatherMiddleware")
        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: MotherMiddleware")

    def __call__(self, request):
        print('This is before view : MotherMiddleware')
        response = self.get_response(request)
        print("This is after view : MotherMiddleware")
        return response


class GrandFatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: GrandFatherMiddleware")

    def __call__(self, request):
        print('This is before view : GrandFatherMiddleware')
        response = self.get_response(request)
        print("This is after view : GrandFatherMiddleware")
        return response


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: BrotherMiddleware")

    def __call__(self, request):
        print('This is before view : BrotherMiddleware')
        response = self.get_response(request)
        print("This is after view : BrotherMiddleware")
        return response


class SisterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: SisterMiddleware")

    def __call__(self, request):
        print('This is before view : SisterMiddleware')
        response = self.get_response(request)
        print("This is after view : SisterMiddleware")
        return response
