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
        # logging.info('Value of {}: {}'.format(tag, value))

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
    url = 'http://192.168.2.95:8000/api/ci-data/test-connection'
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
def call_create_api(current_datetime):

    current_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:00.000')
    
    data_set  = dss.openDataset(conn, 'ITEM_VAL',['NAME','ITEM_VALUE'], 'ru')
    record_BatchNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_BATCH_BUF')
    print('BatchNo DATA: {}'.format(record_BatchNo))
    # logging.info('BatchNo DATA: {}'.format(record_BatchNo))

    # write_logs(record_HMI201_BATCH_BUF)
    record_OrderNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_ORDER_BUF')
    print('OrderNo DATA: {}'.format(record_OrderNo))
    # logging.info('OrderNo DATA: {}'.format(record_OrderNo))
    # logging.info(record_OrderNo)
    # write_logs(record_HMI201_ORDER_BUF)
    record_ProductId     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_PROD_BUFF')
    print('ProductId DATA: {}'.format(record_ProductId))
    # logging.info('ProductId DATA: {}'.format(record_ProductId))
    # write_logs(record_HMI201_PROD_BUFF)
    record_FillNo     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_FILL_BUF')
    print('FillNo DATA: {}'.format(record_FillNo))
    # logging.info('FillNo DATA: {}'.format(record_FillNo))
    # write_logs(record_HMI201_FILL_BUF)
    record_OperatorId     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_OPER_BUFF')
    print (record_OperatorId)
    # logging.info(record_OperatorId)
    # write_logs(record_HMI201_OPER_BUFF)
    record_BatchStart = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI203_TRG_SET')
    print (record_BatchStart)
    # logging.info(record_BatchStart)
    # write_logs(record_TANK01_BATCH)
    record_BatchStop  = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.HMI204_TRG_SET')
    print (record_BatchStop)
    # logging.info(record_BatchStop)




    record_TANK01_BATCH = dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01_BATCH')
    print (record_TANK01_BATCH)
    # logging.info(record_TANK01_BATCH)

    record_TANK01_CT    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01_CT')
    print (record_TANK01_CT)
    # logging.info(record_TANK01_CT)
    record_TANK01LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01LR_STR')
    print (record_TANK01LR_STR)
    # logging.info(record_TANK01LR_STR)
    record_TANK01LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK01LR_STP')
    print (record_TANK01LR_STP)
    # logging.info(record_TANK01LR_STP)




    record_TANK02_BATCH     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02_BATCH')
    print (record_TANK02_BATCH)
    # logging.info(record_TANK02_BATCH)

    record_TANK02_CT     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02_CT')
    print (record_TANK02_CT)
    # logging.info(record_TANK02_CT)

    record_TI003_PV    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI003_PV')
    print (record_TI003_PV)
    # logging.info(record_TI003_PV)

    record_PI014_PV     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.PI014_PV')
    print (record_PI014_PV)
    # logging.info(record_PI014_PV)

    record_TI014_PV    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI014_PV')
    print (record_TI014_PV)
    # logging.info(record_TI014_PV)

    record_TANK02LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02LR_STR')
    print (record_TANK02LR_STR)
    # logging.info(record_TANK02LR_STR)

    record_TANK02LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK02LR_STP')
    print (record_TANK02LR_STP)
    # logging.info(record_TANK02LR_STP)


    record_TANK03_BATCH     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03_BATCH')
    print (record_TANK03_BATCH)
    # logging.info(record_TANK03_BATCH)

    record_TANK03_CT    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03_CT')
    print (record_TANK03_CT)
    # logging.info(record_TANK03_CT)

    record_TI005_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI005_PV')
    print (record_TI005_PV)
    # logging.info(record_TI005_PV)

    record_VSD04_I    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD04_I')
    print (record_VSD04_I)
    # logging.info(record_VSD04_I)

    record_VSD04_S    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD04_S')
    print (record_VSD04_S)
    # logging.info(record_VSD04_S)

    record_TANK03LR_STR    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03LR_STR')
    print (record_TANK03LR_STR)
    # logging.info(record_TANK03LR_STR)

    record_TANK03LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03LR_STP')
    print (record_TANK03LR_STP)
    # logging.info(record_TANK03LR_STP)




    record_TANK04_BATCH    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK04_BATCH')
    print (record_TANK04_BATCH)
    # logging.info(record_TANK04_BATCH)

    record_TANK04_CT   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK04_CT')
    print (record_TANK04_CT)
    # logging.info(record_TANK04_CT)

    record_TI008_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI008_PV')
    print (record_TI008_PV)
    # logging.info(record_TI008_PV)

    record_VSD05_I    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD05_I')
    print (record_VSD05_I)
    # logging.info(record_VSD05_I)

    record_VSD05_S   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD05_S')
    print (record_VSD05_S)
    # logging.info(record_VSD05_S)

    record_TANK04LR_STR    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK04LR_STR')
    print (record_TANK04LR_STR)
    # logging.info(record_TANK04LR_STR)

    record_TANK04LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK04LR_STP')
    print (record_TANK04LR_STP)
    # logging.info(record_TANK04LR_STP)


    # TANK05 K2

    record_TANK05_BATCH     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05_BATCH')
    print (record_TANK05_BATCH)
    # logging.info(record_TANK05_BATCH)

    record_TANK03_CT    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03_CT')
    print (record_TANK03_CT)
    # logging.info(record_TANK03_CT)

    record_TI005_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI005_PV')
    print (record_TI005_PV)
    # logging.info(record_TI005_PV)

    record_VSD04_I    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD04_I')
    print (record_VSD04_I)
    # logging.info(record_VSD04_I)

    record_VSD04_S    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD04_S')
    print (record_VSD04_S)
    # logging.info(record_VSD04_S)

    record_TANK03LR_STR    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03LR_STR')
    print (record_TANK03LR_STR)
    # logging.info(record_TANK03LR_STR)

    record_TANK03LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK03LR_STP')
    print (record_TANK03LR_STP)
    # logging.info(record_TANK03LR_STP)



    #  Tank 6 K3
    record_TANK06_BATCH    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK06_BATCH')
    print (record_TANK06_BATCH)
    # logging.info(record_TANK06_BATCH)

    record_TANK06_CT   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK06_CT')
    print (record_TANK06_CT)
    # logging.info(record_TANK06_CT)

    record_TI908_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI908_PV')
    print (record_TI908_PV)
    # logging.info(record_TI908_PV)

    record_VSD07_I    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD07_I')
    print (record_VSD07_I)
    # logging.info(record_VSD07_I)

    record_VSD07_S   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.VSD07_S')
    print (record_VSD07_S)
    # logging.info(record_VSD07_S)

    record_TANK06LR_STR    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK06LR_STR')
    print (record_TANK06LR_STR)
    # logging.info(record_TANK06LR_STR)

    record_TANK06LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK06LR_STP')
    print (record_TANK06LR_STP)
    # logging.info(record_TANK06LR_STP)


    # Filling

    filling_TANK05_BATCH    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05_BATCH')
    print (filling_TANK05_BATCH)
    # logging.info(filling_TANK05_BATCH)

    filling_TANK05_CT   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05_CT')
    print (filling_TANK05_CT)
    # logging.info(filling_TANK05_CT)

    filling_TI005_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI005_PV')
    print (filling_TI005_PV)
    # logging.info(filling_TI005_PV)

    filling_PT_001    	= dss.readEqual(conn, data_set, 'GREASE2.HOMOGENIZER.PT_001')
    print (filling_PT_001)
    # logging.info(filling_PT_001)

    filling_TI015_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI015_PV')
    print (filling_TI015_PV)
    # logging.info(filling_TI015_PV)

    filling_TI008_PV    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI008_PV')
    print (filling_TI008_PV)
    # logging.info(filling_TI008_PV)

    filling_TANK05LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05LR_STR')
    print (filling_TANK05LR_STR)
    # logging.info(filling_TANK05LR_STR)

    filling_TANK05LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05LR_STP')
    print (filling_TANK05LR_STP)
    # logging.info(filling_TANK05LR_STP)

    # filling2

    filling2_TANK07_BATCH    	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK07_BATCH')
    print (filling2_TANK07_BATCH)
    # logging.info(filling2_TANK07_BATCH)

    filling2_TANK05_CT   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK05_CT')
    print (filling2_TANK05_CT)
    # logging.info(filling2_TANK05_CT)

    filling2_TI908_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI908_PV')
    print (filling2_TI908_PV)
    # logging.info(filling2_TI908_PV)

    filling2_PT_001    	= dss.readEqual(conn, data_set, 'GREASE2.HOMOGENIZER.PT_001')
    print (filling2_PT_001)
    # logging.info(filling2_PT_001)

    filling2_TI015_PV   	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TI015_PV')
    print (filling2_TI015_PV)
    # logging.info(filling2_TI015_PV)


    filling2_TANK07LR_STR     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK07LR_STR')
    print (filling2_TANK07LR_STR)
    # logging.info(filling2_TANK07LR_STR)

    filling2_TANK07LR_STP     	= dss.readEqual(conn, data_set, 'GREASE2.FCX0103.TANK07LR_STP')
    print (filling2_TANK07LR_STP)
    # logging.info(filling2_TANK07LR_STP)


    print("CALL CREATE API START PROCESS NOW !! >>>>>>>>>>>>>>>>>>>>>>>>>>")

   
    
    # batch_no = tag_values.get('GREASE.FAM0101.HMI201_BATCH_BUF', 'default_batch_no')
    # order_no = tag_values.get('GREASE.FAM0101.HMI201_ORDER_BUF', 'default_order_no')
    # Add other tag values as needed

    url = 'http://192.168.2.95:8000/api/ci-data/add-ci-data'
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
        "tank3_k1_batch_no": record_TANK03_BATCH['ITEM_VALUE'],
        "tank3_k1_trig": record_TANK03_CT['ITEM_VALUE'],
        "tank3_k1_t": record_TI005_PV['ITEM_VALUE'],
        "tank3_k1_i": record_VSD04_I['ITEM_VALUE'],
        "tank3_k1_s": record_VSD04_S['ITEM_VALUE'],
        "tank3_k1_start": record_TANK03LR_STR['ITEM_VALUE'],
        "tank3_k1_stop": record_TANK03LR_STP['ITEM_VALUE'],
        "tank3_k1_custom3": 0.00,
        "tank3_k1_custom4": 0.00,
        "tank4_k2_batch_no": record_TANK04_BATCH['ITEM_VALUE'],
        "tank4_k2_trig": record_TANK04_CT['ITEM_VALUE'],
        "tank4_k2_t": record_TI008_PV['ITEM_VALUE'],
        "tank4_k2_i": record_VSD05_I['ITEM_VALUE'],
        "tank4_k2_s": record_VSD05_S['ITEM_VALUE'],
        "tank4_k2_start": record_TANK04LR_STR['ITEM_VALUE'],
        "tank4_k2_stop": record_TANK04LR_STP['ITEM_VALUE'],
        "tank4_k2_custom3": 0.00,
        "tank4_k2_custom4": 0.00,
        "tank5_filling1_batch_no": filling_TANK05_BATCH['ITEM_VALUE'],
        "tank5_filling1_trig": filling_TANK05_CT['ITEM_VALUE'],
        "tank5_filling1_fill_t": filling_TI005_PV['ITEM_VALUE'],
        "tank5_filling1_homo_p": filling_PT_001['ITEM_VALUE'],
        "tank5_filling1_homo_t": filling_TI015_PV['ITEM_VALUE'],
        "tank5_filling1_fill_t2": filling_TI008_PV['ITEM_VALUE'],
        "tank5_filling1_start": filling_TANK05LR_STR['ITEM_VALUE'],
        "tank5_filling1_stop": filling_TANK05LR_STP['ITEM_VALUE'],
        "tank5_filling1_custom3": 0.00,
        "tank5_filling1_custom4": 0.00,
        "tank6_k3_batch_no": record_TANK06_BATCH['ITEM_VALUE'],
        "tank6_k3_trig": record_TANK06_CT['ITEM_VALUE'],
        "tank6_k3_t": record_TI908_PV['ITEM_VALUE'],
        "tank6_k3_i": record_VSD07_I['ITEM_VALUE'],
        "tank6_k3_s": record_VSD07_S['ITEM_VALUE'],
        "tank6_k3_start": record_TANK06LR_STR['ITEM_VALUE'],
        "tank6_k3_stop": record_TANK06LR_STP['ITEM_VALUE'],
        "tank6_k3_custom3": 0.00,
        "tank6_k3_custom4": 0.00,
        "tank7_filling2_batch_no": filling2_TANK07_BATCH['ITEM_VALUE'],
        "tank7_filling2_trig": filling2_TANK05_CT['ITEM_VALUE'],
        "tank7_filling2_fill_t": filling2_TI908_PV['ITEM_VALUE'],
        "tank7_filling2_homo_p": filling2_PT_001['ITEM_VALUE'],
        "tank7_filling2_homo_t": filling2_TI015_PV['ITEM_VALUE'],
        "tank7_filling2_start": filling2_TANK07LR_STR['ITEM_VALUE'],
        "tank7_filling2_stop": filling2_TANK07LR_STP['ITEM_VALUE'],
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
        print("POST DATA {} ".format(data) )
        # logging.info('POST DATA: {}'.format(data))

        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        if response.status_code == 200:
            print("CALL TEST API SUCCESS !!")
            # print(response.json())  # Assuming the response is JSON, print or process it accordingly
            # logging.info('CALL TEST API SUCCESS !! data : {}'.format())
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


# def connect():
#     try:
#         conn = dss.connect()
#         return conn
#     except Exception as e:
#         print("CANNOT CONNECT CI !! !! >>>>>>>>>>>>>>>>>>>>>>>>>>")
#         logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#         error_message = '{} : problem with script or manual: {}'.format(logs_now, e)
#         print(error_message)
#         logging.error(error_message)
#         raise e

if __name__ == "__main__":
    
    print("START OPC CLIENT NOW !! !! >>>>>>>>>>>>>>>>>>>>>>>>>>")
   
    setup_logging()
    conn = dss.connect()
    logging.info('START OPC CLIENT NOW !! !! >>>>>>>>>>>>>>>>>>>>>>>>>>')
    logging.info('CI DSS CONCECTED ')
    while True:
        try:
            # print("START PROCESS NOW !! !! >>>>>>>>>>>>>>>>>>>>>>>>>>")
            # logging.info('START PROCESS NOW !!')
            # tag_values = read_tags()  # Uncomment this line when ready to use tag values
            # call_create_api(tag_values)

            # Define the timezone
            tz = pytz.timezone('Asia/Bangkok')

            # Get the current datetime in the specified timezone
            current_datetime_24 = datetime.now(tz)

            # Get the current datetime
            current_datetime = datetime.now()


            # Format the current datetime to include only minutes and seconds (MM:SS)
            current_MM_SS = current_datetime.strftime('%M:%S')


            current_MM_S000 = current_datetime.strftime('%M:%S')


            if current_MM_S000 == "00:00":
                call_create_api(current_datetime_24)
                print('00 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('00 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "01:00":
                call_create_api(current_datetime_24)
                print('01 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('01 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "02:00":
                call_create_api(current_datetime_24)
                print('02 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('02 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "03:00":
                call_create_api(current_datetime_24)
                print('03 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('03 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "04:00":
                call_create_api(current_datetime_24)
                print('04 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('04 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "05:00":
                call_create_api(current_datetime_24)
                print('05 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('05 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "06:00":
                call_create_api(current_datetime_24)
                print('06 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('06 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "07:00":
                call_create_api(current_datetime_24)
                print('07 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('07 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "08:00":
                call_create_api(current_datetime_24)
                print('08 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('08 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "09:00":
                call_create_api(current_datetime_24)
                print('09 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('09 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "10:00":
                call_create_api(current_datetime_24)
                print('10 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('10 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "11:00":
                call_create_api(current_datetime_24)
                print('11 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('11 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "12:00":
                call_create_api(current_datetime_24)
                print('12 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('12 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "13:00":
                call_create_api(current_datetime_24)
                print('13 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('13 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "14:00":
                call_create_api(current_datetime_24)
                print('14 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('14 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "15:00":
                call_create_api(current_datetime_24)
                print('15 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('15 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "16:00":
                call_create_api(current_datetime_24)
                print('16 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('16 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "17:00":
                call_create_api(current_datetime_24)
                print('17 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('17 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "18:00":
                call_create_api(current_datetime_24)
                print('18 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('18 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "19:00":
                call_create_api(current_datetime_24)
                print('19 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('19 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "20:00":
                call_create_api(current_datetime_24)
                print('20 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('20 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "21:00":
                call_create_api(current_datetime_24)
                print('21 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('21 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "22:00":
                call_create_api(current_datetime_24)
                print('22 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('22 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "23:00":
                call_create_api(current_datetime_24)
                print('23 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('23 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "24:00":
                call_create_api(current_datetime_24)
                print('24 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('24 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "25:00":
                call_create_api(current_datetime_24)
                print('25 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('25 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "26:00":
                call_create_api(current_datetime_24)
                print('26 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('26 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "27:00":
                call_create_api(current_datetime_24)
                print('27 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('27 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "28:00":
                call_create_api(current_datetime_24)
                print('28 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('28 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "29:00":
                call_create_api(current_datetime_24)
                print('29 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('29 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "30:00":
                call_create_api(current_datetime_24)
                print('30 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('30 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "31:00":
                call_create_api(current_datetime_24)
                print('31 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('31 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "32:00":
                call_create_api(current_datetime_24)
                print('32 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('32 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "33:00":
                call_create_api(current_datetime_24)
                print('33 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('33 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "34:00":
                call_create_api(current_datetime_24)
                print('34 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('34 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "35:00":
                call_create_api(current_datetime_24)
                print('35 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('35 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "36:00":
                call_create_api(current_datetime_24)
                print('END 36 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('36 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "37:00":
                call_create_api(current_datetime_24)
                print('END 37 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('37 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "38:00":
                call_create_api(current_datetime_24)
                print('END 38 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('38 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "39:00":
                call_create_api(current_datetime_24)
                print('END 39 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('39 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "40:00":
                call_create_api(current_datetime_24)
                print('END 40 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('40 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "41:00":
                call_create_api(current_datetime_24)
                print('END 41 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('41 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "42:00":
                call_create_api(current_datetime_24)
                print('END 42 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('42 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "43:00":
                call_create_api(current_datetime_24)
                print('END 43 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('43 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "44:00":
                call_create_api(current_datetime_24)
                print('END 44 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('44 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "45:00":
                call_create_api(current_datetime_24)
                print('END 45 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('45 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "46:00":
                call_create_api(current_datetime_24)
                print('END 46 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('46 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "47:00":
                call_create_api(current_datetime_24)
                print('END 47 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('47 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "48:00":
                call_create_api(current_datetime_24)
                print('END 48 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('48 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "49:00":
                call_create_api(current_datetime_24)
                print('END 49 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('49 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "50:00":
                call_create_api(current_datetime_24)
                print('END 50 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('50 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "51:00":
                call_create_api(current_datetime_24)
                print('END 51 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('51 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "52:00":
                call_create_api(current_datetime_24)
                print('END 52 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('52 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "53:00":
                call_create_api(current_datetime_24)
                print('END 53 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('53 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "54:00":
                call_create_api(current_datetime_24)
                print('END 54 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('54 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "55:00":
                call_create_api(current_datetime_24)
                print('END 55 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('55 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "56:00":
                call_create_api(current_datetime_24)
                print('END 56 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('56 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "57:00":
                call_create_api(current_datetime_24)
                print('END 57 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('57 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "58:00":
                print('START 58 current_MM_S000: {}'.format(current_MM_S000))
                call_create_api(current_datetime_24)
                print('END 58 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('58 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            elif current_MM_S000 == "59:00":
                print('START 59 current_MM_S000: {}'.format(current_MM_S000))
                call_create_api(current_datetime_24)
                print('END 59 current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('59 current_MM_S000: {}'.format(current_MM_S000))
                countdown(5)
            # else:
                # print('NO Match current_MM_S000: {}'.format(current_MM_S000))
                # logging.info('NO Match current_MM_S000: {}'.format(current_MM_S000))

            # countdown()
        except Exception as e:
            logs_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            error_message = '{} : problem with script or manual: {}'.format(logs_now, e)
            print(error_message)
            logging.error(error_message)
