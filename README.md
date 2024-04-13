# Fast API Playground with Dependency Injection (DI)
1.  Build API endpoints using Fast API using [Python Dependency Injector](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html)

2. The main advantages of using DI:
    #### Separation of Concerns: The application setup is separated from the actual application logic, making it easier to manage and maintain.

    #### Dependency Injection: The use of the Container class allows for better management of dependencies and provides a way to swap out different implementations of components (e.g., Database) without modifying the rest of the application code.

    #### Modularity: The application is organized into modules (user, product), each with its own endpoints module containing the routes and endpoint handlers. This promotes better code organization and reusability.

---
## `src` folder structure
- `main.py` 
    - main entry point on `create_app` FastAPI
        ```
        def create_app() -> FastAPI:
            container = Container()

            ...

            app = FastAPI()
            app.container = container
        ```
        The container instance is attached to the app object as an attribute: `app.container = container`. This allows access to the container and its managed components throughout the application.
    
- `database.py` 
    - manages a connection to a database using SQLAlchemy
    - `session` : callable object with act as a contect manager a.k.a. "middle person" whenever want to interact with the database.
    - `Singleton` provider reference -> [here](https://refactoring.guru/design-patterns/singleton)
- `containers.py` 
    - responsible for wiring up the different component of the whole app and managing their dependency
    - e.g: `user_repository`: This attribute is a factory provider that creates instances of the `UserRepository` class. The `session_factory` argument is provided by `db.provided.session`, which returns a session factory (a callable that creates database sessions).

- `user`, `product` subfolders - contain all the information on the modules: models, Pydantic schemas, services, endpoint (FastAPI route), repositories (all the logic including interact with the database session)







## command
```docker-compose build``` - to build the docker image

```docker-compose up``` - run the docker images

```alembic init alembic``` - create migration folder

```alembic revision --autogenerate -m "New Migration"``` - like Django makemigration 

```alembic upgrade head``` - like Django migrate (create) the table in the db



# Todo
1. Unit test