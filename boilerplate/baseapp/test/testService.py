from .testModels import *
def testSaveService(**kwargs):
    print('testSaveService', kwargs)
    data = kwargs.get('data')
    testDb=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    action = data.pop('action', 0)
    if id:
        testDb = test.objects.get(pk=id)
        if action:
            testDb.delete()
            testDb=None
        else:
            for key, value in data.items():
                setattr(testDb, key, value)
            testDb.save()
    else:
        testDb = test.objects.create(**data)
    return testDb