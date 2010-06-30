from django.db import models

# Create your models here.
from unique_model.models import UniqueModel

class Role(UniqueModel):
    """
    Role 
    ====

    """

    

    def has_perm(self, permission):
        pass
    



class RolesField(models.Field):
    description="A list of roles"

    def __init__(self, *args, **kwords):
        
