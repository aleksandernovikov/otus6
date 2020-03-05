from typing import List, Optional, Union

import graphene
from django.db.models import QuerySet
from graphene_django import DjangoObjectType

from .models import UniversityUser


class UniversityUserType(DjangoObjectType):
    class Meta:
        model = UniversityUser


class UniversityUserMutation(graphene.Mutation):
    """
    Мутация UniversityUser
    """
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        id = graphene.ID()

    university_user = graphene.Field(UniversityUserType)

    # https://www.python.org/dev/peps/pep-0484/#arbitrary-argument-lists-and-default-argument-values
    def mutate(self, *args: str, **kwargs: int):
        """
        Изменение пользователя по id
        """
        pk: int = kwargs.pop('id')
        user: QuerySet = UniversityUser.objects.filter(pk=pk)
        user.update(**kwargs)

        return UniversityUserMutation(university_user=user.first())


class Mutation(graphene.ObjectType):
    update_user = UniversityUserMutation.Field()


class Query:
    all_users: graphene.List = graphene.List(UniversityUserType, limit=graphene.Int())
    user: graphene.Field = graphene.Field(UniversityUserType, id=graphene.Int())

    @staticmethod
    def resolve_all_users(*args: str, **kwargs: int) -> Union[QuerySet, List[UniversityUser]]:
        """
        Получение всех пользователей
        """
        return UniversityUser.objects.all()[:kwargs.get('limit')]

    @staticmethod
    def resolve_user(*args: str, **kwargs: int) -> Optional[UniversityUser]:
        """
        Получение одного пользователя по id
        """
        pk: int = kwargs.get('id')
        if pk is not None:
            return UniversityUser.objects.get(pk=pk)
        return None
