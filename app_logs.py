from datetime import datetime
import time
import csv 
import dss
import logging

import requests
from requests.exceptions import HTTPError, Timeout, RequestException

def logging_tags():
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
conn = dss.connect()
logs_now_read_tag = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
logs_data = ['Conncet DSS Pass !!!',logs_now_read_tag]
print (logs_data)
logging.info(logs_data)

def read_tag():
    #fields = dss.getFieldNames(conn , 'ITEM_VAL')
    fields       = dss.getFieldNames(conn , 'ITEM_VAL')
    # print (fields)
    #data_set = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'r')
    data_set    	= dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'ru')
    record_HMI201_BATCH_BUF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_BATCH_BUF')
    print (record_HMI201_BATCH_BUF)
    logging.info(record_HMI201_BATCH_BUF)
    # write_logs(record_HMI201_BATCH_BUF)
    record_HMI201_ORDER_BUF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_ORDER_BUF')
    print (record_HMI201_ORDER_BUF)
    logging.info(record_HMI201_ORDER_BUF)
    # write_logs(record_HMI201_ORDER_BUF)
    record_HMI201_PROD_BUFF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_PROD_BUFF')
    print (record_HMI201_PROD_BUFF)
    logging.info(record_HMI201_PROD_BUFF)
    # write_logs(record_HMI201_PROD_BUFF)
    record_HMI201_FILL_BUF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_FILL_BUF')
    print (record_HMI201_FILL_BUF)
    logging.info(record_HMI201_FILL_BUF)
    # write_logs(record_HMI201_FILL_BUF)
    record_HMI201_OPER_BUFF     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.HMI201_OPER_BUFF')
    print (record_HMI201_OPER_BUFF)
    logging.info(record_HMI201_OPER_BUFF)
    # write_logs(record_HMI201_OPER_BUFF)
    record_TANK01_BATCH     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.TANK01_BATCH')
    print (record_TANK01_BATCH)
    logging.info(record_TANK01_BATCH)
    # write_logs(record_TANK01_BATCH)
    record_T010_TI12_GR     	= dss.readEqual(conn, data_set, 'GREASE.FAM0101.T010_TI12_GR')
    print (record_T010_TI12_GR)
    logging.info(record_T010_TI12_GR)
    # write_logs(record_T010_TI12_GR)
    # logging_tags()

def write_logs(logs_data):
    this_moment = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    with open('logs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([this_moment,logs_data])

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat)
        # print()
        # print("GeeksforGeeks", end= ' ')
        time.sleep(1)
        time_sec -= 1

def call_test_api():
    print("CALL TEST API START PROCESS NOW !! >>>>>>>>>>>>>>>>>>>>>>>>>>")
    # Define the URL and the data to be sent
    url = 'http://192.168.2.88:8000/api/ci-data/add-ci-data'
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, timeout=10)  # 10 seconds timeout

        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()


        # Check the response
        print("CALL TEST API SUCCESS !! >>>>>>>>>>>>>>>>>>>>>>>>>>", response.json())

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # HTTP error response (e.g., 404, 500)
        logging.info(f'HTTP error occurred: {http_err}')
    except Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')  # Request timed out
    except RequestException as req_err:
        print(f'Request exception occurred: {req_err}')  # General request exception
    except Exception as err:
        print(f'An error occurred: {err}')  # Any other exceptions

def call_create_api():
    print("CALL CREATE API START PROCESS NOW !! >>>>>>>>>>>>>>>>>>>>>>>>>>")
    # Define the URL and the data to be sent
    url = 'http://192.168.2.88:8000/api/ci-data/add-ci-data'
    data = {
        "time_ci_report" : "2024-06-01T07:01:00.000Z",
        "batch_no" : "20000001",
        "order_no" : "1000001",
        "product_id" : 1,
        "fill_no" : "3000001",
        "operator_id" : 5,
        "batch_start" : 0,
        "batch_stop" : 0,
        "tank1_v1_batch_no" : "0",
        "tank1_v1_trig" : 0,
        "tank1_v1_start" : 0,
        "tank1_v1_stop" : 0,
        "tank1_v1_custom3" : 0.00,
        "tank1_v1_custom4" : 0.00,
        "tank2_a1_batch_no" : "0",
        "tank2_a1_trig" : 0,
        "tank2_a1_t" : 31.00,
        "tank2_a1_p" : 0.00,
        "tank2_a1_oil_t" : 0,
        "tank2_a1_start" : 0,
        "tank2_a1_stop" : 0,
        "tank2_a1_custom3" : 0.00,
        "tank2_a1_custom4" : 0.00,
        "tank3_k1_batch_no" : "0",
        "tank3_k1_trig" : 0,
        "tank3_k1_t" : 0.00,
        "tank3_k1_i" : 0.00,
        "tank3_k1_s" : 0.00,
        "tank3_k1_start" : 0,
        "tank3_k1_stop" : 0,
        "tank3_k1_custom3" : 0.00,
        "tank3_k1_custom4" : 0.00,
        "tank4_k2_batch_no" : "0",
        "tank4_k2_trig" : 0,
        "tank4_k2_t" : 31.00,
        "tank4_k2_i" : 0.00,
        "tank4_k2_s" : 0.00,
        "tank4_k2_start" : 0,
        "tank4_k2_stop" : 0,
        "tank4_k2_custom3" : 0.00,
        "tank4_k2_custom4" : 0.00,
        "tank5_filling1_batch_no" : "0",
        "tank5_filling1_trig" : 0,
        "tank5_filling1_fill_t" : 31.00,
        "tank5_filling1_homo_p" : 0.00,
        "tank5_filling1_homo_t" : 31.00,
        "tank5_filling1_fill_t2": 0,
        "tank5_filling1_start" : 0,
        "tank5_filling1_stop" : 0,
        "tank5_filling1_custom3" : 0.00,
        "tank5_filling1_custom4" : 0.00,
        "tank6_k3_batch_no" : "0",
        "tank6_k3_trig" : 0,
        "tank6_k3_t" : 31.00,
        "tank6_k3_i" : 0.00,
        "tank6_k3_s" : 0.00,
        "tank6_k3_start" : 0,
        "tank6_k3_stop" : 0,
        "tank6_k3_custom3" : 0.00,
        "tank6_k3_custom4" : 0.00,
        "tank7_filling2_batch_no" : "0",
        "tank7_filling2_trig" : 0,
        "tank7_filling2_fill_t" : 31.00,
        "tank7_filling2_homo_p" : 0.00,
        "tank7_filling2_homo_t" : 31.00,
        "tank7_filling2_start" : 0,
        "tank7_filling2_stop" : 0,
        "tank7_filling2_custom3" : 0.00,
        "tank7_filling2_custom4" : 0.00,
        "remark" : "-",
        "is_delete" : 0,
        "is_active" : 1,
        "created_by" : 1,
        "created_at" : "2024-06-21T02:40:40.267Z",
        "updated_at" : "2024-06-21T02:40:40.267Z"
    }
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        # Make the POST request
        response = requests.post(url, json=data, headers=headers, timeout=10)  # 10 seconds timeout

        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        # Check the response
        print("CALL CREATE API SUCCESS !! >>>>>>>>>>>>>>>>>>>>>>>>>>", response.json())

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # HTTP error response (e.g., 404, 500)
        logging.info(f'HTTP error occurred: {http_err}')
    except Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')  # Request timed out
    except RequestException as req_err:
        print(f'Request exception occurred: {req_err}')  # General request exception
    except Exception as err:
        print(f'An error occurred: {err}')  # Any other exceptions


while(True):
    try:
        logging.basicConfig(format='%(asctime)s %(message)s',filename='myapp.log', level=logging.INFO)
        print("START PROCESS NOW !!")
        logging.info('START PROCESS NOW !!')
        read_tag()  
        countdown(60)
        print("END PROCESS !!")
        logging.info('END PROCESS !!')
    except:
        error_python = "{} : problem with script or manual !!!"
        print(error_python.format(logs_now))
        logging.error(': problem with script or manual !!!')
        # print('problem with script or manual !!!')

