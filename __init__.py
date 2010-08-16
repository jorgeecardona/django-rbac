
# from django.conf import settings
# import mongoengine as mongo

# mongo.connect(
#     'ubidots', 
#     username='ubidots',
#     password='ubidots',
#     host='flame.mongohq.com',
#     port=27073)


from django.http import HttpResponseRedirect

class RBACMiddleware(object):
    def process_request(self, request):

        if '_rbac_subject' in request.session:
            request.subject = request.session['_rbac_subject']
        else:
            request.subject = None


def login_required(*args, **kwargs):
    """
    This function decorate a request in order to check if there is a user logged in.
    """

    def new_f(request, *args, **kwargs):
        if '_rbac_subject' in request.session:
            return f(request, *args, **kwargs)

        return HttpResponseRedirect(redirect)

    def dec(f):
        return new_f

    redirect = kwargs.get('redirect', '/accounts/login')

    if (len(args) > 0) and callable(args[0]):
        # Is a decorator without arguments.
        f = args[0]
        return new_f
    
    return dec



                
