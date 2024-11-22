from associates import Associate    
from utils.models import get_object_or_none
from django.conf import settings


user_model = settings.AUTH_USER_MODEL

# returns false if it fails to do its task
def add_associate(from_user, to_user, relationship_type):
    to_user = get_object_or_none(user_model, pk=to_user.pk)
    from_user = get_object_or_none(user_model, pk=from_user.pk)

    if to_user and from_user:
        return Associate.objects.create(
            from_user=from_user,
            to_user=to_user,
            relationship_type=relationship_type
        )

    return False

def remove_associate(from_user, to_user, relationship_type):
    obj = get_object_or_none(
        Associate, 
        from_user=from_user,
        to_user=to_user,
        relationship_type=relationship_type
    )

    if obj:
       return obj.delete() 

    return False