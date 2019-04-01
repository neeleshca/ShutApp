Setup a virtual environment first and install requirements.txt<br>
python3 -m venv env<br>
source ./env/bin/activate (To activate virtual enviornment)<br>
pip install -r requirements.txt<br>


Redis server should be running as the __init__.py file expects a redis connection.

Run the script sh file for the unit tests.<br>
./unit_tests.sh<br>
jm.png is a test image

Run the redis queue to handle background tasks. (execute following command in the flaskr directory)<br>
rq worker save-image<br>

The images are saved in the static folder.<br>
The username is unique, hence the file is stored as {username}.extension <br>
Two folders are present, one for original image(If the person wants to do view image for example) and one for resized image(200x200)<br>
all images are resized, even if they're smaller to maintain consistency<br>


set the flask variables<br>
export FLASK_APP=flaskr<br>
export FLASK_ENV=development (For development mode)<br>

Use <br>
flask init-db <br>
to initialize and clear the database<br>

flask run <br>
to run the flask file <br>

There's a simple HTML form to input username and image. Can be accessed by going to root ("/") of the server.
It's run on the flask server for now, it can be deployed on a docker container(production server) if necessary. 
