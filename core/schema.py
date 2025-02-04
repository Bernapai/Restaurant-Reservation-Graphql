import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
  
schema = graphene.Schema(query=Query)