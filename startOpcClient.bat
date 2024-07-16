@ECHO OFF 

echo Start Run OPC Client V1.00

timeout /t 2

d:

echo D:
timeout /t 2

echo cd D:\Program\github\python_dss_ci
cd D:\Program\github\python_dss_ci
timeout /t 2

start C:\Python2718\python.exe app_ci2.py
