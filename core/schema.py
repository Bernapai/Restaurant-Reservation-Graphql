import graphene
from graphene_django.types import DjangoObjectType
from restaurant.models import Restaurant, Table, Order    

class RestaurantType(graphene.ObjectType):
    class meta:
        model = Restaurant
        fields = ("name", "description")

class TableType(graphene.ObjectType):
    class meta:
        model = Table
        fields = "__all__"

class OrderType(graphene.ObjectType):
    class meta:
        model = Order
        fields = "__all__"

    
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    all_restaurants = graphene.List(RestaurantType)
    all_tables = graphene.List(TableType)
    all_orders = graphene.List(OrderType)
    one_restaurant = graphene.Field(RestaurantType, name=graphene.String())
    one_table = graphene.Field(TableType, number=graphene.Int())
    one_order = graphene.Field(OrderType, id=graphene.Int())


    def get_all(self, info):
        try:
            Model = info.return_type.graphene_type._meta.model
            return Model.objects.all()
        except AttributeError:
            raise ValueError("El tipo no tiene un modelo Django asociado.")
    
    def get_one(self, info, **kwargs):
        try:
            Model = info.return_type.graphene_type._meta.model
            if not kwargs:
                raise ValueError("Debes proporcionar al menos un criterio de búsqueda.")
            return Model.objects.get(**kwargs)
        except AttributeError:
            raise ValueError("El tipo no tiene un modelo Django asociado.")
        except Model.DoesNotExist:
            return None
        except Exception as e:
            raise ValueError(f"Error inesperado: {str(e)}")


    

schema = graphene.Schema(query=Query)