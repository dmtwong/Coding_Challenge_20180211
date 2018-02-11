# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:10:44 2018

@author: David Wong
"""

import os
import collections 
import datetime

os.getcwd()
os.chdir(os.getcwd() + '\\git_projects\\donation-analytics-master\\insight_testsuite\\tests\\test_1\\input')

def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%m%d%Y')
        return True
    except ValueError:
        return False

def validate_zip(zip_n):
    try:
        int(zip_n) # if cannot then False by exception case
        return len(zip_n) >= 5 # False again if can be int but less than 5
    except:
        return False 
    
def empty_key(id_n, name_n, txn_amt):
    if (id_n in ['', None]) or (name_n in ['', None]) or (txn_amt == ''):
        return True
    else:
        return False   

def check_indiv(other_id_n):
    if (other_id_n in ['', None]):
        return True
    else:
        return False

#### Main
sele_var = collections.namedtuple('sele_var', \
                                  'CMTE_ID NAME ZIP_CODE TRANSACTION_DT TRANSACTION_AMT OTHER_ID')

#input_file = open(os.getcwd() + '/Desktop/itcont.txt')               
input_file = open(os.getcwd() + '/itcont.txt')       
output_file = open(os.getcwd() +'/repeat_donors.txt', 'w')

for line in input_file:
    tmp = line.split('|')
    tmp_2 = sele_var(tmp[0], tmp[7], tmp[10], tmp[13], tmp[14], tmp[15])
    if (empty_key(tmp_2[0], tmp_2[1], tmp_2[4]) == True or
        validate_date(tmp_2[3]) == False or
        validate_zip(tmp_2[2]) == False or
        check_indiv(tmp_2[5]) == False):
        continue
    tmp_2 = sele_var(tmp_2[0], tmp_2[1], tmp_2[2][:5], tmp[3], tmp_2[4], tmp[5])
    year_tmp = tmp_2[4][:4]
    output_file.write(tmp_2.CMTE_ID + '|' + tmp_2.NAME + '|' + tmp_2.ZIP_CODE + '|' 
                 + tmp_2.TRANSACTION_DT + '|' + tmp_2.TRANSACTION_AMT + 
                 tmp_2.OTHER_ID + '\n')
    #output_file.write(str(tmp_2))
output_file.close()

#### Archived Unit Test ####    
#### Testing for validate_date()
## Simple Case
result_succ = validate_date(str(01032017))
result_fail = validate_date(str(13032017))
print result_succ, result_fail

## Loop case
test_date_list = [] 
input_file = open(os.getcwd() + '/Desktop/itcont.txt')        
for line in input_file:
    tmp = line.split('|')
    test_date_list.append(str(tmp[13]) )
test_date_list[3] = 'abc'
test_date_list[4] = '0230'
for date in test_date_list:
    if validate_date(date) == False:
        continue
    print date
    
#### Testing for validate_zip()
## Simple Case
result_succ = validate_zip(str(12345))
result_succ2 = validate_zip(str(100001))
result_fail = validate_zip('')
result_fail2 = validate_zip(str(1234))
print result_succ, result_succ2, result_fail, result_fail2

## Loop case
test_zip_list = [] 
input_file = open(os.getcwd() + '/Desktop/itcont.txt')        
for line in input_file:
    tmp = line.split('|')
    test_zip_list.append(str(tmp[10]) )
test_zip_list[3] = 'abc'
test_zip_list[4] = '023'
test_zip_list
for zip_n in test_zip_list:
    if validate_zip(zip_n) == False:
        continue
    print zip_n

#### Testing for empty_key()
## Simple Case
tmp1 = '123' 
tmp2 = 'asdd'
tmp3 = 'abc'   
tmp4 = None
tmp5 = ''
result_succ = empty_key(tmp1,tmp2,tmp3) 
result_fail = empty_key(tmp1,tmp4,tmp3) 
result_fail2 = empty_key(tmp1,tmp5,tmp3) 
print result_succ, result_fail, result_fail2

## Loop case
test_empty_list = [] 
input_file = open(os.getcwd() + '/Desktop/itcont.txt')        
for line in input_file:
    tmp = line.split('|')
    test_empty_list.append( (str(tmp[0]), str(tmp[7]), str(tmp[14]) ) )

test_empty_list[2] = list(test_empty_list[2])
test_empty_list[2][0] = None
test_empty_list[2] = tuple(test_empty_list[2])

test_empty_list[3] = list(test_empty_list[3])
test_empty_list[3][1] = ''
test_empty_list[3] = tuple(test_empty_list[3])

test_empty_list

for tuple_list in test_empty_list:
    if empty_key(tuple_list[0], tuple_list[1], tuple_list[2]) == True:
        continue
    print tuple_list

#### Testing for check_indiv()
## Simple Case
result_succ = check_indiv(str(300047357))
result_fail = check_indiv('')
print result_succ, result_fail

## Loop case
test_indiv_list = [] 
input_file = open(os.getcwd() + '/Desktop/itcont.txt')        
for line in input_file:
    tmp = line.split('|')
    test_indiv_list.append(str(tmp[15]) )

test_indiv_list
test_indiv_list[3] = 'abc'
test_indiv_list[4] = '023'
test_indiv_list
for indiv in test_indiv_list:
    if check_indiv(indiv) == False:
        continue
    print 'indiv'