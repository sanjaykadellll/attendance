from .signupModels import *
def signupSaveService(**kwargs):
    print('signupSaveService', kwargs)
    data = kwargs.get('data')
    signupDb=None
    
    id = data.pop('id', 0)
    if id:
        id = int(id)

    action = data.pop('action', 0)
    if id:
        signupDb = signup.objects.get(pk=id)
        if action:
            signupDb.delete()
            signupDb=None
        else:
            for key, value in data.items():
                setattr(signupDb, key, value)
            signupDb.save()
    else:
        signupDb = signup.objects.create(**data)
    return signupDb