-----

# Understanding GraphQL

This project explores the foundations of GraphQL, a powerful query language for APIs, and its implementation in a Django application. We'll build a Customer Relationship Management (CRM) system to understand key concepts like schemas, queries, and mutations, while also exploring advanced features like filtering and security.

The project is structured into three main tasks, starting with a basic setup and progressing to more complex API functionalities.

## Project Overview

**GraphQL** is a query language for your API and a server-side runtime for executing those queries. Unlike traditional REST APIs, GraphQL allows clients to request exactly the data they need, which helps reduce over-fetching and improves performance. This project will use the **`graphene-django`** library to integrate GraphQL into a Django backend.

### Learning Objectives

By the end of this project, you will be able to:

  * Explain the differences between GraphQL and REST  .
  * Define a GraphQL schema with `Types`, `Queries`, and `Mutations`.
  * Set up a GraphQL endpoint in a Django project using `graphene-django`.
  * Implement various mutations for creating and manipulating data.
  * Use `django-filter` to add complex filtering and sorting to your queries.
  * Interact with a GraphQL API using tools like GraphiQL.

## Setup and Installation

### Prerequisites

  * Python 3.8+
  * Django 3.2+

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/alx-backend-graphql-crm
    cd alx-backend-graphql-crm
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install graphene-django django-filter
    ```
4.  **Configure Django:**
    Add the necessary apps to your `alx-backend-graphql-crm/settings.py` file:
    ```python
    # alx-backend-graphql-crm/settings.py

    INSTALLED_APPS = [
        ...
        'crm',
        'graphene_django',
        'django_filters',
        ...
    ]
    ```

## Tasks

### 0\. Set Up GraphQL Endpoint

**Objective:** Create a basic GraphQL endpoint and define your first schema.

**Instructions:**

1.  Create a Django project named `alx-backend-graphql-crm` and an app named `crm`.
2.  In `alx-backend-graphql-crm/schema.py`, define a `Query` class with a single field named `hello` that returns the string `"Hello, GraphQL!"`.
3.  In your `urls.py`, configure the `GraphQLView` with `graphiql=True` at the `/graphql` endpoint to enable the browser-based API explorer.

**Checkpoint:**

Verify your setup by navigating to `http://localhost:8000/graphql` and running the following query:

```graphql
query {
  hello
}
```

### 1\. Build and Seed a CRM Database with GraphQL Integration

**Objective:** Implement mutations to create `Customer`, `Product`, and `Order` objects with robust validation and error handling.

**Instructions:**

1.  **Define Models:** Create `Customer`, `Product`, and `Order` models in `crm/models.py`. The `Order` model should have a many-to-many relationship with `Product` and a foreign key to `Customer`.
2.  **Define Mutations:** In `crm/schema.py`, create the following mutation classes:
      * **`CreateCustomer`**: A single customer with validation for unique email and phone number format.
      * **`BulkCreateCustomers`**: Accepts a list of customer inputs and supports partial success.
      * **`CreateProduct`**: A new product with validation for positive price and non-negative stock.
      * **`CreateOrder`**: An order with nested product associations, calculating the `total_amount` automatically.
3.  **Integrate Mutations:** Add these mutation fields to a `Mutation` class in `crm/schema.py` and then combine it with the main schema in `alx-backend-graphql-crm/schema.py`.

**Checkpoint:**

Test your mutations using the following example queries in GraphiQL:

```graphql
# Create a single customer
mutation {
  createCustomer(input: {
    name: "Alice",
    email: "alice@example.com",
    phone: "+1234567890"
  }) {
    customer {
      id
      name
      email
      phone
    }
    message
  }
}

# Create a product
mutation {
  createProduct(input: {
    name: "Laptop",
    price: 999.99,
    stock: 10
  }) {
    product {
      id
      name
      price
      stock
    }
  }
}
```

### 2\. Add Filtering

**Objective:** Allow users to search and filter customer, product, and order data using a variety of criteria.

**Instructions:**

1.  **Install and Configure `django-filter`**: Ensure `django_filters` is in your `INSTALLED_APPS`.
2.  **Create Filter Classes**: In `crm/filters.py`, define `CustomerFilter`, `ProductFilter`, and `OrderFilter` classes using `django-filter`'s `FilterSet` to provide filtering capabilities for fields like `name` (case-insensitive), `email`, `price` (range), and `total_amount` (range).
3.  **Integrate Filters with GraphQL**: In `crm/schema.py`, update your `Query` class to use `graphene-django`'s `DjangoFilterConnectionField` for `all_customers`, `all_products`, and `all_orders` queries. This will automatically expose filter arguments to your GraphQL schema.

**Checkpoint:**

Test your filtering functionality with these queries in GraphiQL:

```graphql
# Filter customers by a partial name match
query {
  allCustomers(filter: { nameIcontains: "Ali" }) {
    edges {
      node {
        id
        name
      }
    }
  }
}

# Filter products by a price range
query {
  allProducts(filter: { priceGte: 100, priceLte: 1000 }) {
    edges {
      node {
        id
        name
        price
      }
    }
  }
}
```