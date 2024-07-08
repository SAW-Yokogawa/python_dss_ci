from datetime import datetime
import time
import csv 
import dss
import logging

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

