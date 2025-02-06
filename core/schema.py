import graphene
from graphene_django.types import DjangoObjectType
from restaurant.models import Restaurant, Table, Order    

class RestaurantType(graphene.DjangoObjectType):
    class meta:
        model = Restaurant
        fields = ("name", "description")

class TableType(graphene.DjangoObjectType):
    class meta:
        model = Table
        fields = "__all__"

class OrderType(graphene.DjangoObjectType):
    class meta:
        model = Order
        fields = "__all__"



#Metodos de mutacion POST
class CreateRestaurantMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
    Restaurant = graphene.Field(RestaurantType)
    
    def mutate(self, info, name, description):
        restaurant = Restaurant(name=name, description=description)
        restaurant.save()
        return CreateRestaurantMutation(restaurant=restaurant)

class CreateTableMutation(graphene.Mutation):
    class Arguments:
        number = graphene.Int()
        restaurant = graphene.String()
        quantity = graphene.Int()
    Table = graphene.Field(TableType)
    
    def mutate(self, info, number, restaurant, quantity):
        table = Table(number=number, restaurant=restaurant, quantity=quantity)
        table.save()
        return CreateTableMutation(table=table)

class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        table = graphene.Int()
        restaurant = graphene.String()
        order_time = graphene.String()
    Order = graphene.Field(OrderType)
    
    def mutate(self, info, table, restaurant, order_time):
        order = Order(table=table, restaurant=restaurant, order_time=order_time)
        order.save()
        return CreateOrderMutation(order=order)
    



#Metodos de consulta DEL
class DeleteRestaurantMutation(graphene.Mutation):
    pass

class DeleteTableMutation(graphene.Mutation):
    pass

class DeleteOrderMutation(graphene.Mutation):
    pass






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





class Mutation(graphene.ObjectType):
    CreateRestaurant = CreateRestaurantMutation.Field()
    CreateTable = CreateTableMutation.Field()
    CreateOrder = CreateOrderMutation.Field()
    DeleteRestaurant = DeleteRestaurantMutation.Field()
    DeleteTable = DeleteTableMutation.Field()
    DeleteOrder = DeleteOrderMutation.Field()
    

schema = graphene.Schema(query=Query)