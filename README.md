# Fintech App

# Setup PostgreSQL server

psql -U postgres -h localhost -p 5432                   // login to PostgreSQL
CREATE DATABASE fintechdb;                              // create Database
\l                                                      // list databases
exit                                                    // come out of PostgreSQL
psql -U postgres -d fintechdb -h localhost -p 5432      // login to PostgreSQL with given database
-------------------------------------------------------------------------------------------------------

# Run flask app locally
D:\Labs\Capstone projects\fintech_app_db_integration-capstone-project>code .
# make sure to uncomment the code under api\__init__.py before running below commands
	$env:FLASK_APP="api"  
	$env:FLASK_RUN_HOST="127.0.0.1"    
	$env:FLASK_ENV="development"   
	flask run

# Running on http://127.0.0.1:5000
# Go to PostgreSQL and check table is created by running below command 
\d

# goto postman and try to run POST command for http://localhost:5000/register with following JSON code.
{
  "username": "12",
  "password": "testpass"
}

# Go to PostgreSQL and check user is created by running below command
SELECT * FROM users;

------------------------------------
# Run flask app using dockerfile


docker build -t fintech_app:V4 .
docker run --env-file .env -p 5000:5000 fintech_app:V4
or
# to register new user, run docker command with "host.docker.internal" user instead of localhost

docker run -e 'DB_URL="postgresql://postgres:Word2Vec@host.docker.internal:5432/fintechdb:V4"' -p 5000:5000 fintech_app:V4









