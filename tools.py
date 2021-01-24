# functions for converting the bank statements

import os.path
import json
import pandas as pd
import datetime
start_date = '2021-01-01'
end_date = '2021-01-17'

from __future__ import print_function
import pickle
import os.path
from Google import Create_Service

CLIENT_SECRET_FILE = ""
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ['https://www.googleapis.com/auth/drive']

# service = 

def main():
    # get google account keys
    with open('keys.json') as f:
        allKeys = json.load(f)

    # read bank statement csv
    statementDF = pd.read_csv(allKeys['statement_filepath'])

    # convert Date to datetime format for easier date filtering
    statementDF["Date"] = pd.to_datetime(statementDF.Date)

    # filter out the days from the statement
    datedStatementDF = statementDF.loc[(statementDF['Date'] > start_date) & (statementDF['Date'] <= end_date)]

    # filter out income from paychecks (need to be more specific for all income transactions, limited to paycheck as of this version)
    paycheckDF = datedStatementDF.loc[(datedStatementDF['Category'] == 'Paycheck') | (datedStatementDF['Category'] == 'Income') ]

    # filter out all transactions that aren't paycheck
    expensesDF = datedStatementDF.loc[(datedStatementDF['Category'] != 'Paycheck') & (datedStatementDF['Category'] != 'Income')]

    categoryList =  expensesDF['Category'].unique()

    



    print("paycheckDF")
    print(paycheckDF)
    print("expensesDF")
    print(expensesDF)
    print("categories")
    print(categoryList)

if __name__ == 'main':
    main()