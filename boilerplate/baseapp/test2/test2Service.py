from .test2Models import *
def test2SaveService(**kwargs):
    print('test2SaveService', kwargs)
    data = kwargs.get('data')
    test2Db=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    markedToDelete_ = data.pop('markedToDelete_', 0)
    if id:
        test2Db = test2.objects.get(pk=id)
        if markedToDelete_:
            test2Db.delete()
            test2Db=None
        else:
            for key, value in data.items():
                setattr(test2Db, key, value)
            test2Db.save()
    else:
        test2Db = test2.objects.create(**data)
    return test2Db