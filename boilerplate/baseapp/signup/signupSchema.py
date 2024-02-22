import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from .signupModels import *
from .signupService import *

class signupType(DjangoObjectType):
    class Meta:
        model = signup

class signupInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    post = graphene.String()
    password = graphene.String()
    confirmpassword = graphene.String()
    action = graphene.String()


class signup_SaveMutation(graphene.Mutation):
    class Arguments:
        data = signupInput()

    signup_Obj = graphene.Field(lambda: signupType)

    def mutate(self, info, data):
        dbsignup = signupSaveService(data=data)
        return signup_SaveMutation(signup_Obj=dbsignup)