# build-pulse-project

#Project Details
  - Domain: Car Dealership
  - Interface: Web API


#Install
Requirements:
  - python 2.7
  - pip
    - ubuntu: ```sudo apt-get isntall python-pip```
  - virtualenv
    - ubuntu: ```pip install virtualenv```

cd into project_folder

Run commands below in order inside the base project folder
```
export FLASK_APP=build_pulse
export FLASK_DEBUG=true
virtualenv build_pulse
source build_pulse/bin/activate
pip install --editable .
flask init-db
```

#Run
```
flask run
```

#Test
```
python setup.py test
```

#Endpoints
- localhost:5000
- Get '/' returns all cars in stock
- Post '/' takes a json object with the following properties
The one required field operator takes a value 'AND' or 'OR'
```
{
    "properties" : {
        "make": { "type": "string" },
        "year": { "type": "number" },
        "color": { "type": "string" },
        "price": { "type": "number" },
        "hasSunroof": { "type": "string" },
        "isFourWheelDrive": { "type": "string" },
        "hasLowMiles": { "type": "string" },
        "hasPowerWindows": { "type": "string" },
        "hasNavigation": { "type": "string" },
        "hasHeatedSeats": { "type": "string" },
        "operation": { "type": "string" },
    },
    "required": ["operator"]
}
```
