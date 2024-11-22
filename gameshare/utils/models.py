# for some reason django raises an error if the 
# object you are querying does not exists so
# I made this util function that returns None if
# object does not exists
def get_object_or_none(model, **kwargs):
    try:
        model.object.get(**kwargs)
    except model.DoesNotExist:
        return None
    except Exception as e:
        raise e