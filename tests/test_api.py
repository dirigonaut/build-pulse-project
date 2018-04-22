import pytest
import json
from flask import g, session
from build_pulse import get_app
from build_pulse.db import get_db

client = get_app().test_client()

def test_get_all_stock():
    assert client.get('/').status_code == 200

def test_get_stock_schema_validation():
    payload = {"hasPowerWindows":"true"}
    headers = {'Content-Type' : 'application/json'}
    response = client.post('/', data=json.dumps(payload), headers=headers)
    assert response.status_code == 400

def test_get_stock_schema_extra_fields():
    payload = {"hasPowerWindows":"true","operator":"OR","test":"test"}
    headers = {'Content-Type' : 'application/json'}
    response = client.post('/', data=json.dumps(payload), headers=headers)
    assert response.status_code == 400

def test_get_stock_and():
    payload = {"color":"Silver","hasPowerWindows":"true","operator":"AND"}
    headers = {'Content-Type' : 'application/json'}
    response = client.post('/', data=json.dumps(payload), headers=headers)
    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]["_id"] == '59d2698c05889e0b23959106'


def test_get_stock_or():
    payload = {"color":"Silver","hasPowerWindows":"true","operator":"OR"}
    headers = {'Content-Type' : 'application/json'}
    response = client.post('/', data=json.dumps(payload), headers=headers)
    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 5
    print data
    assert data[0]["_id"] == '59d2698c05889e0b23959106'
    assert data[1]["_id"] == '59d2698c6f1dc2cbec89c413'
    assert data[2]["_id"] == '59d2698c340f2728382c0a73'
    assert data[3]["_id"] == '59d2698ce2e7eeeb4f109001'
    assert data[4]["_id"] == '59d2698cd6a3b8f0dd994c9d'
