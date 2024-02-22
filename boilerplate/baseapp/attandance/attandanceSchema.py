import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from .attandanceModels import *
from .attandanceService import *

class attandanceType(DjangoObjectType):
    class Meta:
        model = attandance

class attandanceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    checkin = graphene.String()
    checkout = graphene.String()
    time = graphene.DateTime()
    post = graphene.String()
    action = graphene.Int()


class attandance_SaveMutation(graphene.Mutation):
    class Arguments:
        data = attandanceInput()

    attandance_Obj = graphene.Field(lambda: attandanceType)

    def mutate(self, info, data):
        dbattandance = attandanceSaveService(data=data)
        return attandance_SaveMutation(attandance_Obj=dbattandance)