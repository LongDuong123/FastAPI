architecture : microservice 

Service:
    - Controller : Validate the accessToken for authentication/authorization , Define and manage API routes.
    - Service :  Implement the business logic.
    - Repository :  Interact with databases.
    - Test :  Contain unit tests for individual components.
    - Model : Define data structures.

Lib:
    - Reusable functions that can be shared across multiple services.

infra/base:
    - Used to load Python libraries and source code.