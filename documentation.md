# Notes about the project

## How to run the tests

- If the tests are run for the first time, you need to build the docker-compose with the environment variable set to "STAGING" once to initialize the database tables in the test_db.

```docker exec -it <container_name> pytest```
