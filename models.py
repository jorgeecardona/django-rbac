from django.db import models
from django.utils import simplejson

# Create your models here.
#from unique_model.models import UniqueModel

class ListStringField(models.TextField):
    
    description = "A list of strings."

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        if not ('default' in kwargs):
            kwargs['default'] = simplejson.dumps([])

        super(ListStringField, self).__init__(*args, **kwargs)
    
    def to_python(self, value):
        if isinstance(value, list) and all([isinstance(x, (str, unicode)) for x in value]):
            return value

        value = simplejson.loads(value)
        if isinstance(value, list) and all([isinstance(x, (str, unicode)) for x in value]):
            return value
        
        return []
        
    def get_prep_value(self, value):
        return simplejson.dumps(value)

class Agent(models.Model):
    """
    Agent
    =====

    This is an abstract class that define the minimum aspects 
    to be an agent in Role-Based Access Control.

    It define a basic list of roles, this roles are basically identified with the name of the role.
    
    """

    class Meta(object):
        abstract = True

    roles = ListStringField()
