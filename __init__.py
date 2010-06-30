from django.contrib.auth.models import User

class RBACMiddleware(object):
    def process_request(self, request):

        # Fetch user and profile.
        if hasattr(request, 'user'):
            if isinstance(request.user, User):
                request.profile = request.user.get_profile()
                

                
