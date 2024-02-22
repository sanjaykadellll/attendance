from .attandanceModels import *
def attandanceSaveService(**kwargs):
    print('attandanceSaveService', kwargs)
    data = kwargs.get('data')
    attandanceDb=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    action = data.pop('action', 0)
    if id:
        attandanceDb = attandance.objects.get(pk=id)
        if action:
            attandanceDb.delete()
            attandanceDb=None
        else:
            for key, value in data.items():
                setattr(attandanceDb, key, value)
            attandanceDb.save()
    else:
        attandanceDb = attandance.objects.create(**data)
    return attandanceDb