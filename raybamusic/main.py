import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


app = FastAPI()
schema = graphene.Schema(query=Query)
app.add_route("/", GraphQLApp(schema=schema))
