import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from .test2Models import *
from .test2Service import *

class test2Type(DjangoObjectType):
    class Meta:
        model = test2

class test2Input(graphene.InputObjectType):
    id = graphene.ID()
    firstname1 = graphene.String()
    lastname2 = graphene.String()
    email1 = graphene.String()
    address1 = graphene.String()
    remark1 = graphene.Int()
    markedToDelete_ = graphene.Int()


class test2_SaveMutation(graphene.Mutation):
    class Arguments:
        data = test2Input()

    test2_Obj = graphene.Field(lambda: test2Type)

    def mutate(self, info, data):
        dbtest2 = test2SaveService(data=data)
        return test2_SaveMutation(test2_Obj=dbtest2)