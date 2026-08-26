from django.shortcuts import redirect


class BlockExpiredOTPAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path == '/verify-otp/':

            if 'otp' not in request.session:
                return redirect('forgot_password')

        response = self.get_response(request)

        return response