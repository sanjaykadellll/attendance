from baseapp.models import *
def detailSaveService(**kwargs):
    print('detailSaveService', kwargs)
    data = kwargs.get('data')
    detailDb=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    markedToDelete_ = data.pop('markedToDelete_', 0)
    if id:
        detailDb = detail.objects.get(pk=id)
        if markedToDelete_:
            detailDb.delete()
            detailDb=None
        else:
            for key, value in data.items():
                setattr(detailDb, key, value)
            detailDb.save()
    else:
        detailDb = detail.objects.create(**data)
    return detailDb