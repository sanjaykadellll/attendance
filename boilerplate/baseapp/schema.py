import graphene
from graphene import ObjectType, String, Decimal, Int, Date
from graphene_django import DjangoObjectType
from baseapp.detail.detailModels import detail
from baseapp.detail.detailSchema import detailType, detail_SaveMutation

from baseapp.test.testModels import test
from baseapp.test.testSchema import testType, test_SaveMutation

from baseapp.test2.test2Models import test2
from baseapp.test2.test2Schema import test2Type, test2_SaveMutation

from baseapp.signup.signupModels import signup
from baseapp.signup.signupSchema import signupType, signup_SaveMutation

from baseapp.attandance.attandanceModels import attandance
from baseapp.attandance.attandanceSchema import attandanceType, attandance_SaveMutation


class Query(ObjectType):
    detail = graphene.List(detailType)
    test = graphene.List(testType)
    test2 = graphene.List(test2Type)
    signup = graphene.List(signupType)
    attandance = graphene.List(attandanceType)

    def resolve_detail(self, info):
        return detail.objects.all()
    def resolve_test(self,info):
        return test.objects.all()

    def resolve_test2(self,info):
        return test2.objects.all()

    def resolve_signup(self,info):
        return signup.objects.all()

    def resolve_attandance(self,info):
        return attandance.objects.all()
    
    def resolve_checkin(self, info):
        return self.checkin

    def resolve_checkout(self, info):
        return self.checkout

class Mutation(graphene.ObjectType):
    save_detail = test_SaveMutation.Field()
    save_test = test_SaveMutation.Field()
    save_test2 = test2_SaveMutation.Field()
    signup = signup_SaveMutation.Field()
    attandance = attandance_SaveMutation.Field()
    

schema = graphene.Schema(query=Query, mutation=Mutation)




