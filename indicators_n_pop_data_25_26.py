"""
@author: peter.saiu@nhs.net
Created: 2024
version: 0.1.2
Updated on 31/5/2025 with data for 2025/26 (which includes Indicators from 2023/24 and GP population for March 2025). 

Description: 
The code in this script imports the population and indicators data which 
are then imported and run in the strealit app ('eFIT')      # 

"""

import pandas as pd

# Indicator and GP population data is for the year: 
year = '2025-26'

# Import the indicators data
indicators_qox = pd.read_csv(f'input_data_ind/QOX_{year}.csv')      # Bath and North East Somerset, Swindon and Wiltshire ICB
indicators_qhg = pd.read_csv(f'input_data_ind/QHG_{year}.csv')      # Bedfordshire, Luton and Milton Keynes ICB
indicators_qhl = pd.read_csv(f'input_data_ind/QHL_{year}.csv')      # Birmingham and Solihull ICB
indicators_qua = pd.read_csv(f'input_data_ind/QUA_{year}.csv')      # Black Country ICB
indicators_quy = pd.read_csv(f'input_data_ind/QUY_{year}.csv')      # Bristol, North Somerset and South Gloucestershire ICB
indicators_qu9 = pd.read_csv(f'input_data_ind/QU9_{year}.csv')      # Buckinghamshire, Oxfordshire and Berkshire West ICB
indicators_que = pd.read_csv(f'input_data_ind/QUE_{year}.csv')      # Cambridgeshire and Peterborough ICB
indicators_qyg = pd.read_csv(f'input_data_ind/QYG_{year}.csv')      # Cheshire and Merseyside ICB
indicators_qt6 = pd.read_csv(f'input_data_ind/QT6_{year}.csv')      # Cornwall and the Isles of Scilly ICB
indicators_qwu = pd.read_csv(f'input_data_ind/QWU_{year}.csv')      # Coventry and Warwickshire ICB
indicators_qj2 = pd.read_csv(f'input_data_ind/QJ2_{year}.csv')      # Derby and Derbyshire ICB
indicators_qjk = pd.read_csv(f'input_data_ind/QJK_{year}.csv')      # Devon ICB
indicators_qvv = pd.read_csv(f'input_data_ind/QVV_{year}.csv')      # Dorset ICB
indicators_qnq = pd.read_csv(f'input_data_ind/QNQ_{year}.csv')      # Frimley ICB
indicators_qr1 = pd.read_csv(f'input_data_ind/QR1_{year}.csv')      # Gloucestershire ICB
indicators_qop = pd.read_csv(f'input_data_ind/QOP_{year}.csv')      # Greater Manchester ICB
indicators_qrl = pd.read_csv(f'input_data_ind/QRL_{year}.csv')      # Hampshire and the Isle of Wight ICB
indicators_qgh = pd.read_csv(f'input_data_ind/QGH_{year}.csv')      # Herefordshire and Worcestershire ICB
indicators_qm7 = pd.read_csv(f'input_data_ind/QM7_{year}.csv')      # Hertfordshire and West Essex ICB
indicators_qoq = pd.read_csv(f'input_data_ind/QOQ_{year}.csv')      # Humber and North Yorkshire ICB
indicators_qks = pd.read_csv(f'input_data_ind/QKS_{year}.csv')      # Kent and Medway ICB
indicators_qe1 = pd.read_csv(f'input_data_ind/QE1_{year}.csv')      # Lancashire and South Cumbria ICB
indicators_qk1 = pd.read_csv(f'input_data_ind/QK1_{year}.csv')      # Leicester, Leicestershire and Rutland ICB
indicators_qjm = pd.read_csv(f'input_data_ind/QJM_{year}.csv')      # Lincolnshire ICB
indicators_qh8 = pd.read_csv(f'input_data_ind/QH8_{year}.csv')      # Mid and South Essex ICB
indicators_qmm = pd.read_csv(f'input_data_ind/QMM_{year}.csv')      # Norfolk and Waveney ICB
indicators_qmj = pd.read_csv(f'input_data_ind/QMJ_{year}.csv')      # North Central London ICB
indicators_qhm = pd.read_csv(f'input_data_ind/QHM_{year}.csv')      # North East and North Cumbria ICB
indicators_qmf = pd.read_csv(f'input_data_ind/QMF_{year}.csv')      # North East London ICB
indicators_qrv = pd.read_csv(f'input_data_ind/QRV_{year}.csv')      # North West London ICB
indicators_qpm = pd.read_csv(f'input_data_ind/QPM_{year}.csv')      # Northamptonshire ICB
indicators_qt1 = pd.read_csv(f'input_data_ind/QT1_{year}.csv')      # Nottingham and Nottinghamshire ICB
indicators_qoc = pd.read_csv(f'input_data_ind/QOC_{year}.csv')      # Shropshire, Telford and Wrekin ICB
indicators_qsl = pd.read_csv(f'input_data_ind/QSL_{year}.csv')      # Somerset ICB
indicators_qkk = pd.read_csv(f'input_data_ind/QKK_{year}.csv')      # South East London ICB
indicators_qwe = pd.read_csv(f'input_data_ind/QWE_{year}.csv')      # South West London ICB
indicators_qf7 = pd.read_csv(f'input_data_ind/QF7_{year}.csv')      # South Yorkshire ICB
indicators_qnc = pd.read_csv(f'input_data_ind/QNC_{year}.csv')      # Staffordshire and Stoke-on-Trent ICB
indicators_qjg = pd.read_csv(f'input_data_ind/QJG_{year}.csv')      # Suffolk and North East Essex ICB
indicators_qxu = pd.read_csv(f'input_data_ind/QXU_{year}.csv')      # Surrey Heartlands ICB
indicators_qnx = pd.read_csv(f'input_data_ind/QNX_{year}.csv')      # Sussex ICB
indicators_qwo = pd.read_csv(f'input_data_ind/QWO_{year}.csv')      # West Yorkshire ICB


# Import the population data
# Males
m_pop_qox = pd.read_csv(f'input_data_m/m_pop_qox_{year}.csv')      
m_pop_qhg = pd.read_csv(f'input_data_m/m_pop_qhg_{year}.csv')       
m_pop_qhl = pd.read_csv(f'input_data_m/m_pop_qhl_{year}.csv')       
m_pop_qua = pd.read_csv(f'input_data_m/m_pop_qua_{year}.csv')       
m_pop_quy = pd.read_csv(f'input_data_m/m_pop_quy_{year}.csv')       
m_pop_qu9 = pd.read_csv(f'input_data_m/m_pop_qu9_{year}.csv')       
m_pop_que = pd.read_csv(f'input_data_m/m_pop_que_{year}.csv')       
m_pop_qyg = pd.read_csv(f'input_data_m/m_pop_qyg_{year}.csv')       
m_pop_qt6 = pd.read_csv(f'input_data_m/m_pop_qt6_{year}.csv')       
m_pop_qwu = pd.read_csv(f'input_data_m/m_pop_qwu_{year}.csv')       
m_pop_qj2 = pd.read_csv(f'input_data_m/m_pop_qj2_{year}.csv')       
m_pop_qjk = pd.read_csv(f'input_data_m/m_pop_qjk_{year}.csv')       
m_pop_qvv = pd.read_csv(f'input_data_m/m_pop_qvv_{year}.csv')      
m_pop_qnq = pd.read_csv(f'input_data_m/m_pop_qnq_{year}.csv')       
m_pop_qr1 = pd.read_csv(f'input_data_m/m_pop_qr1_{year}.csv')       
m_pop_qop = pd.read_csv(f'input_data_m/m_pop_qop_{year}.csv')       
m_pop_qrl = pd.read_csv(f'input_data_m/m_pop_qrl_{year}.csv')       
m_pop_qgh = pd.read_csv(f'input_data_m/m_pop_qgh_{year}.csv')       
m_pop_qm7 = pd.read_csv(f'input_data_m/m_pop_qm7_{year}.csv')       
m_pop_qoq = pd.read_csv(f'input_data_m/m_pop_qoq_{year}.csv')       
m_pop_qks = pd.read_csv(f'input_data_m/m_pop_qks_{year}.csv')       
m_pop_qe1 = pd.read_csv(f'input_data_m/m_pop_qe1_{year}.csv')       
m_pop_qk1 = pd.read_csv(f'input_data_m/m_pop_qk1_{year}.csv')       
m_pop_qjm = pd.read_csv(f'input_data_m/m_pop_qjm_{year}.csv')       
m_pop_qh8 = pd.read_csv(f'input_data_m/m_pop_qh8_{year}.csv')       
m_pop_qmm = pd.read_csv(f'input_data_m/m_pop_qmm_{year}.csv')       
m_pop_qmj = pd.read_csv(f'input_data_m/m_pop_qmj_{year}.csv')       
m_pop_qhm = pd.read_csv(f'input_data_m/m_pop_qhm_{year}.csv')       
m_pop_qmf = pd.read_csv(f'input_data_m/m_pop_qmf_{year}.csv')       
m_pop_qrv = pd.read_csv(f'input_data_m/m_pop_qrv_{year}.csv')       
m_pop_qpm = pd.read_csv(f'input_data_m/m_pop_qpm_{year}.csv')       
m_pop_qt1 = pd.read_csv(f'input_data_m/m_pop_qt1_{year}.csv')       
m_pop_qoc = pd.read_csv(f'input_data_m/m_pop_qoc_{year}.csv')       
m_pop_qsl = pd.read_csv(f'input_data_m/m_pop_qsl_{year}.csv')       
m_pop_qkk = pd.read_csv(f'input_data_m/m_pop_qkk_{year}.csv')       
m_pop_qwe = pd.read_csv(f'input_data_m/m_pop_qwe_{year}.csv')       
m_pop_qf7 = pd.read_csv(f'input_data_m/m_pop_qf7_{year}.csv')       
m_pop_qnc = pd.read_csv(f'input_data_m/m_pop_qnc_{year}.csv')       
m_pop_qjg = pd.read_csv(f'input_data_m/m_pop_qjg_{year}.csv')       
m_pop_qxu = pd.read_csv(f'input_data_m/m_pop_qxu_{year}.csv')       
m_pop_qnx = pd.read_csv(f'input_data_m/m_pop_qnx_{year}.csv')       
m_pop_qwo = pd.read_csv(f'input_data_m/m_pop_qwo_{year}.csv')       

# Females
f_pop_qox = pd.read_csv(f'input_data_f/f_pop_qox_{year}.csv')       
f_pop_qhg = pd.read_csv(f'input_data_f/f_pop_qhg_{year}.csv')       
f_pop_qhl = pd.read_csv(f'input_data_f/f_pop_qhl_{year}.csv')       
f_pop_qua = pd.read_csv(f'input_data_f/f_pop_qua_{year}.csv')       
f_pop_quy = pd.read_csv(f'input_data_f/f_pop_quy_{year}.csv')       
f_pop_qu9 = pd.read_csv(f'input_data_f/f_pop_qu9_{year}.csv')       
f_pop_que = pd.read_csv(f'input_data_f/f_pop_que_{year}.csv')       
f_pop_qyg = pd.read_csv(f'input_data_f/f_pop_qyg_{year}.csv')       
f_pop_qt6 = pd.read_csv(f'input_data_f/f_pop_qt6_{year}.csv')       
f_pop_qwu = pd.read_csv(f'input_data_f/f_pop_qwu_{year}.csv')       
f_pop_qj2 = pd.read_csv(f'input_data_f/f_pop_qj2_{year}.csv')       
f_pop_qjk = pd.read_csv(f'input_data_f/f_pop_qjk_{year}.csv')       
f_pop_qvv = pd.read_csv(f'input_data_f/f_pop_qvv_{year}.csv')       
f_pop_qnq = pd.read_csv(f'input_data_f/f_pop_qnq_{year}.csv')       
f_pop_qr1 = pd.read_csv(f'input_data_f/f_pop_qr1_{year}.csv')       
f_pop_qop = pd.read_csv(f'input_data_f/f_pop_qop_{year}.csv')       
f_pop_qrl = pd.read_csv(f'input_data_f/f_pop_qrl_{year}.csv')       
f_pop_qgh = pd.read_csv(f'input_data_f/f_pop_qgh_{year}.csv')       
f_pop_qm7 = pd.read_csv(f'input_data_f/f_pop_qm7_{year}.csv')       
f_pop_qoq = pd.read_csv(f'input_data_f/f_pop_qoq_{year}.csv')       
f_pop_qks = pd.read_csv(f'input_data_f/f_pop_qks_{year}.csv')       
f_pop_qe1 = pd.read_csv(f'input_data_f/f_pop_qe1_{year}.csv')       
f_pop_qk1 = pd.read_csv(f'input_data_f/f_pop_qk1_{year}.csv')       
f_pop_qjm = pd.read_csv(f'input_data_f/f_pop_qjm_{year}.csv')       
f_pop_qh8 = pd.read_csv(f'input_data_f/f_pop_qh8_{year}.csv')       
f_pop_qmm = pd.read_csv(f'input_data_f/f_pop_qmm_{year}.csv')       
f_pop_qmj = pd.read_csv(f'input_data_f/f_pop_qmj_{year}.csv')       
f_pop_qhm = pd.read_csv(f'input_data_f/f_pop_qhm_{year}.csv')       
f_pop_qmf = pd.read_csv(f'input_data_f/f_pop_qmf_{year}.csv')       
f_pop_qrv = pd.read_csv(f'input_data_f/f_pop_qrv_{year}.csv')       
f_pop_qpm = pd.read_csv(f'input_data_f/f_pop_qpm_{year}.csv')       
f_pop_qt1 = pd.read_csv(f'input_data_f/f_pop_qt1_{year}.csv')       
f_pop_qoc = pd.read_csv(f'input_data_f/f_pop_qoc_{year}.csv')       
f_pop_qsl = pd.read_csv(f'input_data_f/f_pop_qsl_{year}.csv')       
f_pop_qkk = pd.read_csv(f'input_data_f/f_pop_qkk_{year}.csv')       
f_pop_qwe = pd.read_csv(f'input_data_f/f_pop_qwe_{year}.csv')       
f_pop_qf7 = pd.read_csv(f'input_data_f/f_pop_qf7_{year}.csv')       
f_pop_qnc = pd.read_csv(f'input_data_f/f_pop_qnc_{year}.csv')       
f_pop_qjg = pd.read_csv(f'input_data_f/f_pop_qjg_{year}.csv')       
f_pop_qxu = pd.read_csv(f'input_data_f/f_pop_qxu_{year}.csv')       
f_pop_qnx = pd.read_csv(f'input_data_f/f_pop_qnx_{year}.csv')       
f_pop_qwo = pd.read_csv(f'input_data_f/f_pop_qwo_{year}.csv')       


# do I need to close all these files above now e.g. 'indicators_qox.close()       







