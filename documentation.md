# Notes about the project

## How to run the tests

- If the tests are run for the first time, you need to build the docker-compose with the environment variable set to "STAGING" once to initialize the database tables in the test_db.

```docker exec -it <container_name> pytest```


## How to import the .env values to github secrets

- Install the gh cli tool ```sudo apt install gh``` and authenticate with your github account ```gh auth login```
- Set all values of the .env file as secrets in github ```gh secret set -f .env```


