import mongoengine as mongo
from django.utils import simplejson

# Create your models here.
#from unique_model.models import UniqueModel


"""

Role Based Access Control
=========================

This application build the essential models and function for a django site to
use rbac.

It defines several abtract models:
 
 * Subject: A person or an automated agent.
 * Role: Job function that define an authoritative level.
 * Permission: An approval to access a resource in a particular mode.
 * Session: A session mantain the information of Subject and Role. (django.contrib.sessions)


 Subject
 =======

A subject is an user or an automated agent, as a node or a gadget. 
This model defines two abstract methods:

 * identify: Used to identify a subject given some identification parameters. A site has to define a particular subject model that inherite from Subject and define this function, with its identification parameters.

 * authenticate: Used to authenticate a subject given some authentication parameters.

 Role
 ====

A role is just a job function or a title that define a subsets of subjects. It helps to define the responsabilities of the subjects that belong to this role.

 Permission
 ==========


 Resource
 ========

"""

class Subject(object):

    """
    Subject
    =======

    This is an abstract class that define the minimum aspects 
    to be an agent in Role-Based Access Control.

    It define a basic list of roles, this roles are basically 
    identified with the name of the role.
    """

    #roles = 

    @classmethod
    def identify(cls, *args, **kwargs):
        """
        This method should receive the parameters needed to identify an agent.
        """
        raise NonImplementedException("Define an identification mechanism.")
    
    def authenticate(self, *args, **kwargs):
        raise NonImplementedException(
            "Define an authentication mechanism.")
    
    def authorize(self, *args, **kwargs):
        raise NonImplementedException(
            "Define an authoization mechanism to perform transaction."
            )

    def authenticate_request(self, request, *args, **kwargs):
        self.authenticate(*args, **kwargs)
        request.session['_rbac_subject'] = self

    def deauthenticate_request(self, request):
        request.session.flush()
