# Proyecto: API GraphQL para Gestión de Restaurantes y Reservas

## 📜 Descripción del Proyecto
El proyecto consiste en una API GraphQL que permite a los usuarios buscar restaurantes, consultar la disponibilidad de mesas y realizar reservas. Los restaurantes pueden gestionar sus mesas y horarios, mientras que los usuarios pueden reservar mesas para una fecha y hora específica.

---

## ✨ Funcionalidades Principales

### 🏢 Gestión de Restaurantes
- Registro de restaurantes y gestión de su información (nombre, dirección, horarios, capacidad, etc.).
- Administración del número limitado de mesas disponibles.

### 🔍 Búsqueda de Restaurantes
- Búsqueda de restaurantes por ubicación, tipo de cocina y horarios.
- Consulta de disponibilidad de mesas en una fecha y hora específica.

### 📅 Reservas
- Creación de reservas en restaurantes para una fecha y hora específica.
- Posibilidad de modificar o cancelar reservas.

### 🔐 Autenticación y Autorización
- Registro e inicio de sesión de usuarios para realizar reservas.
- Acceso especial para restaurantes, permitiendo gestionar mesas y reservas.


---

## 🔧 Consultas y Mutaciones GraphQL

### Consultas
- `restaurants`: Listar todos los restaurantes.
- `restaurant(id: ID!)`: Obtener detalles de un restaurante.
- `availableTables(restaurantId: ID!, date: String!)`: Ver mesas disponibles en un restaurante para una fecha específica.

### Mutaciones
- `registerUser(input: UserInput!)`: Registrar un nuevo usuario.
- `loginUser(email: String!, password: String!)`: Iniciar sesión.
- `createReservation(input: ReservationInput!)`: Crear una reserva.
- `cancelReservation(id: ID!)`: Cancelar una reserva.

---

## ⚙️ Tecnologías a Utilizar
- **Django:** Framework principal para el backend.
- **Graphene (o Strawberry):** Para implementar GraphQL.
- **JWT:** Para autenticación de usuarios.
- **MySql/Postgresql/Sqlite3:** Base de datos para almacenar la información.


---

## 🔄 Flujo de Trabajo

### 📲 Registro y Autenticación
- Los usuarios se registran e inician sesión para acceder a las funcionalidades.

### 🔍 Búsqueda y Reserva
- Los usuarios buscan restaurantes y verifican la disponibilidad de mesas.
- Realizan una reserva para una fecha y hora específica.



### ⚙️ Gestión de Restaurantes
- Los dueños de restaurantes pueden gestionar sus mesas y ver las reservas activas.
