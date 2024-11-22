from associates import Associate    
from utils.models import get_object_or_none

# returns false if it fails to do its task
def add_associate(from_user, to_user, relationship_type):
    obj = get_object_or_none(
        Associate, 
        from_user=from_user,
        to_user=to_user,
        relationship_type=relationship_type
    )

    if not obj:
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