# build-pulse-project

#Project Details
  - Domain: Car Dealership
  - Interface: Web API


#Install
Requirements:
  - python 2.7
  - pip
  - virtualenv

cd into project_folder

```
export FLASK_APP=build_pulse
export FLASK_DEBUG=true
virtualenv build_pulse
source build_pulse/bin/activate
pip install --editable .
flask initdb
```

#Run
```
flask run
```

#Test
```
pytest
```

#Endpoints
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
