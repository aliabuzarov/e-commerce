from django.utils.deprecation import MiddlewareMixin

class IpAddressMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        