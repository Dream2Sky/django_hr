from django.utils.deprecation import MiddlewareMixin


class AuditMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        return None