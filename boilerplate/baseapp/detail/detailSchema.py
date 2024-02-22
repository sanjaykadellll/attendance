import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from baseapp.models import *
from .detailService import *

class detailType(DjangoObjectType):
    class Meta:
        model = detail

class detailInput(graphene.InputObjectType):
    id = graphene.ID()
    firstname = graphene.String()
    lastname = graphene.String()
    email = graphene.String()
    address = graphene.String()
    remark = graphene.Int()
    markedToDelete_ = graphene.Int()


class detail_SaveMutation(graphene.Mutation):
    class Arguments:
        data = detailInput()

    detail_Obj = graphene.Field(lambda: detailType)

    def mutate(self, info, data):
        dbdetail = detailSaveService(data=data)
        return detail_SaveMutation(detail_Obj=dbdetail)

       
