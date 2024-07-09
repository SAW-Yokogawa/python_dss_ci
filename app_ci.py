import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from datetime import datetime
import time
import csv
import dss
import logging
import pytz

def setup_logging():
    logging.basicConfig(format='%(asctime)s %(message)s', filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

def read_tag(tag):
    conn = dss.connect()
    fields = dss.getFieldNames(conn, 'ITEM_VAL')
    data_set = dss.openDataset(conn, 'ITEM_VAL', ['NAME', 'ITEM_VALUE'], 'ru')
    record = dss.readEqual(conn, data_set, tag)
    print(record)
    logging.info(record)
    record = dss.readEqual(conn, data_set, tag)
    value = record['ITEM_VALUE']
    print(f"Value Of {tag} : {value}")
    logging.info(f"Value Of {tag} : {value}")
    return value

def write_logs(logs_data):
    this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    with open('logs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([this_moment, logs_data])

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        time_sec -= 1

def call_test_api():
    url = 'http://192.168.2.88:8000/api/ci-data/add-ci-data'
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("CALL TEST API SUCCESS !!", response.json())
    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Timeout as timeout_err:
        logging.error(f'Timeout error occurred: {timeout_err}')
    except RequestException as req_err:
        logging.error(f'Request exception occurred: {req_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')

def call_create_api():

    print("CALL CREATE API START PROCESS NOW !! >>>>>>>>>>>>>>>>>>>>>>>>>>")

    tags = [
        'GREASE.FAM0101.HMI201_BATCH_BUF',
        'GREASE.FAM0101.HMI201_ORDER_BUF',
        'GREASE.FAM0101.HMI201_PROD_BUFF',
        'GREASE.FAM0101.HMI201_FILL_BUF',
        'GREASE.FAM0101.HMI201_OPER_BUFF',
        'GREASE.FAM0101.TANK01_BATCH',
        'GREASE.FAM0101.T010_TI12_GR'
    ]

    for tag in tags:
        read_tag(tag)


    # Get the current datetime in Asia/Bangkok timezone
    tz = pytz.timezone('Asia/Bangkok')
    current_datetime = datetime.now(tz).isoformat()

    batch_no = tag_values.get('GREASE.FAM0101.HMI201_BATCH_BUF', 'default_batch_no')

    url = 'http://192.168.2.88:8000/api/ci-data/add-ci-data'
    data = {
        "time_ci_report": "2024-06-01T07:01:00.000Z",
        "batch_no": "20000001",
        "order_no": "1000001",
        "product_id": 1,
        "fill_no": "3000001",
        "operator_id": 5,
        "batch_start": 0,
        "batch_stop": 0,
        "tank1_v1_batch_no": "0",
        "tank1_v1_trig": 0,
        "tank1_v1_start": 0,
        "tank1_v1_stop": 0,
        "tank1_v1_custom3": 0.00,
        "tank1_v1_custom4": 0.00,
        "tank2_a1_batch_no": "0",
        "tank2_a1_trig": 0,
        "tank2_a1_t": 31.00,
        "tank2_a1_p": 0.00,
        "tank2_a1_oil_t": 0,
        "tank2_a1_start": 0,
        "tank2_a1_stop": 0,
        "tank2_a1_custom3": 0.00,
        "tank2_a1_custom4": 0.00,
        "tank3_k1_batch_no": "0",
        "tank3_k1_trig": 0,
        "tank3_k1_t": 0.00,
        "tank3_k1_i": 0.00,
        "tank3_k1_s": 0.00,
        "tank3_k1_start": 0,
        "tank3_k1_stop": 0,
        "tank3_k1_custom3": 0.00,
        "tank3_k1_custom4": 0.00,
        "tank4_k2_batch_no": "0",
        "tank4_k2_trig": 0,
        "tank4_k2_t": 31.00,
        "tank4_k2_i": 0.00,
        "tank4_k2_s": 0.00,
        "tank4_k2_start": 0,
        "tank4_k2_stop": 0,
        "tank4_k2_custom3": 0.00,
        "tank4_k2_custom4": 0.00,
        "tank5_filling1_batch_no": "0",
        "tank5_filling1_trig": 0,
        "tank5_filling1_fill_t": 31.00,
        "tank5_filling1_homo_p": 0.00,
        "tank5_filling1_homo_t": 31.00,
        "tank5_filling1_fill_t2": 0,
        "tank5_filling1_start": 0,
        "tank5_filling1_stop": 0,
        "tank5_filling1_custom3": 0.00,
        "tank5_filling1_custom4": 0.00,
        "tank6_k3_batch_no": "0",
        "tank6_k3_trig": 0,
        "tank6_k3_t": 31.00,
        "tank6_k3_i": 0.00,
        "tank6_k3_s": 0.00,
        "tank6_k3_start": 0,
        "tank6_k3_stop": 0,
        "tank6_k3_custom3": 0.00,
        "tank6_k3_custom4": 0.00,
        "tank7_filling2_batch_no": "0",
        "tank7_filling2_trig": 0,
        "tank7_filling2_fill_t": 31.00,
        "tank7_filling2_homo_p": 0.00,
        "tank7_filling2_homo_t": 31.00,
        "tank7_filling2_start": 0,
        "tank7_filling2_stop": 0,
        "tank7_filling2_custom3": 0.00,
        "tank7_filling2_custom4": 0.00,
        "remark": "-",
        "is_delete": 0,
        "is_active": 1,
        "created_by": 1,
        "created_at": "2024-06-21T02:40:40.267Z",
        "updated_at": "2024-06-21T02:40:40.267Z"
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        print("CALL CREATE API SUCCESS !!", response.json())
    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Timeout as timeout_err:
        logging.error(f'Timeout error occurred: {timeout_err}')
    except RequestException as req_err:
        logging.error(f'Request exception occurred: {req_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')

setup_logging()

while True:
    try:
        print("START PROCESS NOW !!")
        logging.info('START PROCESS NOW !!')
        read_tag()  
        countdown(60)
        print("END PROCESS !!")
        logging.info('END PROCESS !!')
    except Exception as e:
        logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        error_message = f"{logs_now} : problem with script or manual: {e}"
        print(error_message)
        logging.error(error_message)