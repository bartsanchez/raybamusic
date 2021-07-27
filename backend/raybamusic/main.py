import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)


class Song(SQLAlchemyObjectType):
    class Meta:
        model = models.Song
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_songs = SQLAlchemyConnectionField(Song.connection)


app = FastAPI()
schema = graphene.Schema(query=Query)
app.add_route("/", GraphQLApp(schema=schema))
