import graphene
from graphene_django import DjangoObjectType
from restaurant.models import Restaurant, Table, Order    

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("name", "description")

class TableType(DjangoObjectType):
    class Meta:
        model = Table
        fields = "__all__"

class OrderType(DjangoObjectType):
    class Meta:
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
    class Arguments:
        name = graphene.String()
    Restaurant = graphene.Field(RestaurantType)

    def mutate(self, info, name):
        restaurant = Restaurant.objects.get(name=name)
        restaurant.delete()
        return DeleteRestaurantMutation(restaurant=restaurant)

class DeleteTableMutation(graphene.Mutation):
    class Arguments:
        number = graphene.Int()
    Table = graphene.Field(TableType)

    def mutate(self, info, number):
        table = Table.objects.get(number=number)
        table.delete()
        return DeleteTableMutation(table=table)

class DeleteOrderMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
    Order = graphene.Field(OrderType)

    def mutate(self, info, id):
        order = Order.objects.get(id=id)
        order.delete()
        return DeleteOrderMutation(order=order)





class UpdateRestaurantMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
    Restaurant = graphene.Field(RestaurantType)
    def mutate(self, info, id ,name, description):
        restaurant = Restaurant.objects.get(pk=id)
        restaurant.name = name
        restaurant.description = description
        restaurant.save()
        return UpdateRestaurantMutation(restaurant=restaurant)

class UpdateTableMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        number = graphene.Int()
        restaurant = graphene.String()
        quantity = graphene.Int()
    Table = graphene.Field(TableType)
    def mutate(self, info, id ,number, restaurant, quantity):
        table = Table.objects.get(pk=id)
        table.number = number
        table.restaurant = restaurant
        table.quantity = quantity
        table.save()
        return UpdateTableMutation(table=table)

class UpdateOrderMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        table = graphene.Int()
        restaurant = graphene.String()
        order_time = graphene.String()
    Order = graphene.Field(OrderType)
    def mutate(self, info, id ,table, restaurant, order_time):
        order = Order.objects.get(pk=id)
        order.table = table
        order.restaurant = restaurant
        order.order_time = order_time
        order.save()
        return UpdateOrderMutation(order=order)







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
    UpdateRestaurant = UpdateRestaurantMutation.Field()
    UpdateTable = UpdateTableMutation.Field()
    UpdateOrder = UpdateOrderMutation.Field()
    

schema = graphene.Schema(query=Query)