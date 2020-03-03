import graphene
from graphene_django import DjangoObjectType

from .models import UniversityUser


class UniversityUserType(DjangoObjectType):
    class Meta:
        model = UniversityUser


class UniversityUserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        id = graphene.ID()

    university_user = graphene.Field(UniversityUserType)

    def mutate(self, *args, **kwargs):
        id = kwargs.pop('id')
        user = UniversityUser.objects.get(pk=id)

        for attr, value in kwargs.items():
            setattr(user, attr, value)
        user.save(update_fields=kwargs.keys())

        return UniversityUserMutation(university_user=user)


class Mutation(graphene.ObjectType):
    update_user = UniversityUserMutation.Field()


class Query:
    all_users = graphene.List(UniversityUserType, limit=graphene.Int())
    user = graphene.Field(UniversityUserType, id=graphene.Int())

    def resolve_all_users(self, *args, **kwargs):
        return UniversityUser.objects.all()[:kwargs.get('limit')]

    def resolve_user(self, *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return UniversityUser.objects.get(pk=id)
        return None
