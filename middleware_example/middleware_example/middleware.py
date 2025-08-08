import time
from django.utils.deprecation import MiddlewareMixin


class RequestTimingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()  # store when request starts

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            elapsed_time = time.time() - request.start_time
            print(f":stopwatch: Request to {request.path} took {elapsed_time:.2f} seconds")
        return response