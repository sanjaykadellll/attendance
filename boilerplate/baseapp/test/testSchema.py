import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from .testModels import *
from .testService import *

class testType(DjangoObjectType):
    class Meta:
        model = test

class testInput(graphene.InputObjectType):
    id = graphene.ID()
    firstname1 = graphene.String()
    lastname2 = graphene.String()
    email1 = graphene.String()
    address1 = graphene.String()
    remark1 = graphene.Int()
    action = graphene.Int()


class test_SaveMutation(graphene.Mutation):
    class Arguments:
        data = testInput()

    test_Obj = graphene.Field(lambda: testType)

    def mutate(self, info, data):
        dbtest = testSaveService(data=data)
        return test_SaveMutation(test_Obj=dbtest)