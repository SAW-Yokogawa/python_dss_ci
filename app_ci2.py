import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from datetime import datetime
import time
import csv
import os
import dss
import logging
import pytz

def setup_logging():
    logging.basicConfig(format='%(asctime)s %(message)s', filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)


def read_tags():
    conn = dss.connect()
    fields = dss.getFieldNames(conn, 'ITEM_VAL')
    data_set = dss.openDataset(conn, 'ITEM_VAL', ['NAME', 'ITEM_VALUE'], 'ru')

    tags = [
        'GREASE.FAM0101.HMI201_BATCH_BUF',
        'GREASE.FAM0101.HMI201_ORDER_BUF',
        'GREASE.FAM0101.HMI201_PROD_BUFF',
        'GREASE.FAM0101.HMI201_FILL_BUF',
        'GREASE.FAM0101.HMI201_OPER_BUFF',
        'GREASE.FAM0101.TANK01_BATCH',
        'GREASE.FAM0101.T010_TI12_GR'
    ]

    tag_values = {}
    for tag in tags:
        record = dss.readEqual(conn, data_set, tag)
        value = record['ITEM_VALUE']
        tag_values[tag] = value

        print('Value of {}: {}'.format(tag, value))
        logging.info('Value of {}: {}'.format(tag, value))

    return tag_values

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
    print("CALL TEST API NOW !!")
    url = 'http://192.168.2.88:8000/api/ci-data/test-connection'
    headers = {'Content-Type': 'application/json'}

    try:
        print("START TEST API NOW !!")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("CALL TEST API SUCCESS !!", response.json())
    except HTTPError as http_err:
        logging.error('HTTP error occurred: {}'.format(http_err))
    except Timeout as timeout_err:
        logging.error('Timeout error occurred: {}'.format(timeout_err))
    except RequestException as req_err:
        logging.error('Request exception occurred: {}'.format(req_err))
    except Exception as err:
        logging.error('An error occurred: {}'.format(err))

# def call_create_api(tag_values):
def call_create_api():
    
    data_set  = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'ru')
    record_BatchNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_BATCH_BUF')
    print('BatchNo DATA: {}'.format(record_BatchNo))
    logging.info('BatchNo DATA: {}'.format(record_BatchNo))

    # write_logs(record_HMI201_BATCH_BUF)
    record_OrderNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_ORDER_BUF')
    print('OrderNo DATA: {}'.format(record_OrderNo))
    logging.info('OrderNo DATA: {}'.format(record_OrderNo))
    logging.info(record_OrderNo)
    # write_logs(record_HMI201_ORDER_BUF)
    record_ProductId     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_PROD_BUFF')
    print('ProductId DATA: {}'.format(record_ProductId))
    logging.info('ProductId DATA: {}'.format(record_ProductId))
    # write_logs(record_HMI201_PROD_BUFF)
    record_FillNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_FILL_BUF')
    print('FillNo DATA: {}'.format(record_FillNo))
    logging.info('FillNo DATA: {}'.format(record_FillNo))
    # write_logs(record_HMI201_FILL_BUF)
    record_OperatorId     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_OPER_BUFF')
    print (record_OperatorId)
    logging.info(record_OperatorId)
    # write_logs(record_HMI201_OPER_BUFF)
    record_BatchStart = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_TRG_SET')
    print (record_BatchStart)
    logging.info(record_BatchStart)
    # write_logs(record_TANK01_BATCH)
    record_BatchStop  = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI204_TRG_SET')
    print (record_BatchStop)
    logging.info(record_BatchStop)




    record_TANK01_BATCH = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01_BATCH')
    print (record_TANK01_BATCH)
    logging.info(record_TANK01_BATCH)

    record_TANK01_CT    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01_CT')
    print (record_TANK01_CT)
    logging.info(record_TANK01_CT)
    record_TANK01LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01LR_STR')
    print (record_TANK01LR_STR)
    logging.info(record_TANK01LR_STR)
    record_TANK01LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01LR_STP')
    print (record_TANK01LR_STP)
    logging.info(record_TANK01LR_STP)




    record_TANK02_BATCH     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02_BATCH')
    print (record_TANK02_BATCH)
    logging.info(record_TANK02_BATCH)

    record_TANK02_CT     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02_CT')
    print (record_TANK02_CT)
    logging.info(record_TANK02_CT)

    record_TI003_PV    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI003_PV')
    print (record_TI003_PV)
    logging.info(record_TI003_PV)

    record_PI014_PV     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.PI014_PV')
    print (record_PI014_PV)
    logging.info(record_PI014_PV)

    record_TI014_PV    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI014_PV')
    print (record_TI014_PV)
    logging.info(record_TI014_PV)

    record_TANK02LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02LR_STR')
    print (record_TANK02LR_STR)
    logging.info(record_TANK02LR_STR)

    record_TANK02LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02LR_STP')
    print (record_TANK02LR_STP)
    logging.info(record_TANK02LR_STP)


    

    print("CALL CREATE API START PROCESS NOW !! >>>>>>>>>>>>>>>>>>>>>>>>>>")

    # Define the timezone
    tz = pytz.timezone('Asia/Bangkok')

    # Get the current datetime in the specified timezone
    this_moment = datetime.now(tz)

    # Format the datetime as a string in '%Y-%m-%d %H:%M:%S' format
    current_datetime = this_moment.strftime('%Y-%m-%d %H:%M:000')
    
    # batch_no = tag_values.get('GREASE.FAM0101.HMI201_BATCH_BUF', 'default_batch_no')
    # order_no = tag_values.get('GREASE.FAM0101.HMI201_ORDER_BUF', 'default_order_no')
    # Add other tag values as needed

    url = 'http://192.168.2.88:8000/api/ci-data/add-ci-data'
    data = {
        "time_ci_report": current_datetime,
        "batch_no": record_BatchNo['ITEM_VALUE'],
        "order_no": record_OrderNo['ITEM_VALUE'],
        "product_id": record_ProductId['ITEM_VALUE'],
        "fill_no": record_FillNo['ITEM_VALUE'],
        "operator_id": record_OperatorId['ITEM_VALUE'],
        "batch_start": record_BatchStart['ITEM_VALUE'],
        "batch_stop": record_BatchStop['ITEM_VALUE'],
        "tank1_v1_batch_no": record_TANK01_BATCH['ITEM_VALUE'],
        "tank1_v1_trig": record_TANK01_CT['ITEM_VALUE'],
        "tank1_v1_start": record_TANK01LR_STR['ITEM_VALUE'],
        "tank1_v1_stop": record_TANK01LR_STP['ITEM_VALUE'],
        "tank1_v1_custom3": 0.00,
        "tank1_v1_custom4": 0.00,
        "tank2_a1_batch_no": record_TANK02_BATCH['ITEM_VALUE'],
        "tank2_a1_trig": record_TANK02_CT['ITEM_VALUE'],
        "tank2_a1_t": record_TI003_PV['ITEM_VALUE'],
        "tank2_a1_p": record_PI014_PV['ITEM_VALUE'],
        "tank2_a1_oil_t": record_TI014_PV['ITEM_VALUE'],
        "tank2_a1_start": record_TANK02LR_STR['ITEM_VALUE'],
        "tank2_a1_stop": record_TANK02LR_STP['ITEM_VALUE'],
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
        "created_at": current_datetime,
        "updated_at": current_datetime
    }
    headers = {'Content-Type': 'application/json'}

    try:
        # print("POST DATA {} ".format(data) )
        logging.info('POST DATA: {}'.format(data))

        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        if response.status_code == 200:
            print("CALL TEST API SUCCESS !!")
            # print(response.json())  # Assuming the response is JSON, print or process it accordingly
            logging.info('CALL TEST API SUCCESS !! data : {}'.format())
        else:
            print('Unexpected response from API: Status Code {}'.format(response.status_code))
            logging.error('Unexpected response from API: Status Code {}'.format(response.status_code))
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))
        logging.error('HTTP error occurred: {}'.format(http_err))
        print('Response content: {}'.format(http_err.response.content))
        logging.error('Response content: {}'.format(http_err.response.content))
    except Timeout as timeout_err:
        print('Timeout error occurred: {}'.format(timeout_err))
        logging.error('Timeout error occurred: {}'.format(timeout_err))
    except RequestException as req_err:
        print('Request exception occurred: {}'.format(req_err))
        logging.error('Request exception occurred: {}'.format(req_err))
    except Exception as err:
        print('An error occurred: {}'.format(err))
        logging.error('An error occurred: {}'.format(err))

if __name__ == "__main__":
    setup_logging()
    conn = dss.connect()

    while True:
        try:
            logging.info('START PROCESS NOW !!')
            # tag_values = read_tags()  # Uncomment this line when ready to use tag values
            # call_create_api(tag_values)
            call_create_api()
            countdown(2)
            logging.info('END PROCESS !!')
        except Exception as e:
            logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            error_message = '{} : problem with script or manual: {}'.format(logs_now, e)
            print(error_message)
            logging.error(error_message)
