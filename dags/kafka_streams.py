from datetime import datetime
from airflow import DAG
import json
import requests
from airflow.providers.standard.operators.python import PythonOperator

default_args = {
    "owner": "Wilson",
    "start_date": datetime(2026, 1, 5, 10, 00)
}
def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    street_number = location['street']['number']
    street_name = location['street']['name']
    data['address'] = f"{street_number} {street_name}, {location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data


def stream_data():

    res = get_data()
    res = format_data(res)

    print(json.dumps(res, indent=3))

with DAG('user_automation',
         default_args= default_args,
         schedule = '@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data()