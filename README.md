# Getting Started!
git clone everything<br/>
in app/.env, put in the openweathermap api key<br/>
docker-compose up --build<br/>
in browser, follow http://127.0.0.1:8000/docs# to see swagger doc<br/>

# Schemas
## City
id - auto generated int<br/>
name - str

## AccessHistory
id - auto generated int<br/>
timestamp - datetime, set by db<br/>
city_id - int, foreignkey referencing city <br/>
status = enum, value can be 'success' or 'failure'<br/>


# Structure
using a typical fast api approach with basic 3 tier application architecture without the presentation layer<br/>
database handles db connection<br/>
declared models using sqlalchemy, containing the 2 tables needed<br/>
schemas act as DTO, handles serialization between controller and models (tables)<br/>
crud file contains all the crud methods in and out the db<br/>
service file handles all the business logic, including invoking the weather api<br/>
routers handles http requests and responses, as well as orchestrating services<br/>
unit tests are placed in their own folder, one unit test file per crud, service and controller<br/>
<br/>
main is the app's entry point<br/>
<br/>
this project uses alembic for migrations, alembic.ini doesn't contains the db connection string, they are configured in alembiuc/env.py<br/>


## architecture trade-offs:
1. I left comments in some of files mentioning that a few files can be broken into multiple files when dealing with biggeer application
2. Using interfaces, this is something I would normally do but the time doesn't allow me to imeplement it
In a 3 tier application architecture or DDD pattern, each layer of the project should only interact through interfaces
e.g. controller should call the interface of service class, and the interface of crud classes

None of these are big issues, they can be refactored relatively easily


## Feature Improvement:
### Cities With the same name 
1. currently, openweatherapi will use the most famous city (London from England is picked over London in Ontario, Canada)
2. to resolve this, we can add additional columns for country and state/provice to narrow down which city
3. added basic crud assertion tests using pytest, can add more controller test using httpx



## CI/CD pipeline
1. generated client side sdk, this is something I would do as a part of the stadard, but I didnt' have the time to do it
fastapi already spits out swagger doc so it's very easy to generate by hand using the CLI tool, but this should ideally be a part of the pipeline
2. gating, adding gating as a part of the pipeline for more quality control, and can prevent costly errors going into production
3. credential manager, in this localhost exercise, I added my secret in env file, which is only half of what production should look like. 
We can make this better by using a credential manager, I've used Azure Key Vault, Azure Library, we can also do google secret manager, and retrieve the secret as a part of the deployment pipeline, this way secrets would be not be shared in any way during deployment


## More Error Handling
1. when 3rd party API is involved, it is important to implemented rollback mechanism similar to what's being used in distributed system
2. need to add more unit testings but out of time
