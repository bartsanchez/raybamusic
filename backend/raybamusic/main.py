import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from . import crud, models
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)


class Song(SQLAlchemyObjectType):
    class Meta:
        model = models.Song


class Query(graphene.ObjectType):
    songs = graphene.List(Song)

    def resolve_songs(self, info):
        session = info.context.get("session", SessionLocal)
        return crud.get_all_songs(session)


app = FastAPI()
schema = graphene.Schema(query=Query)
app.add_route("/", GraphQLApp(schema=schema))
