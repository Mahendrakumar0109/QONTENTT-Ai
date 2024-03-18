# app/schema.py
from .schema import schema
from graphene import ObjectType, String, Int, Schema, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import User

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = User

class Query(ObjectType):
    users = List(UserSchema)

    def resolve_users(self, info):
        return User.query.all()

class Mutation(ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)
