# functions for converting the bank statements

import os.path
import json
import pandas as pd
import datetime
start_date = '2021-01-01'
end_date = '2021-01-17'



# get google account keys
with open('keys.json') as f:
    allKeys = json.load(f)

# read bank statement csv
statementDF = pd.read_csv(allKeys['statement_filepath'])

# convert Date to datetime format for easier date filtering
statementDF["Date"] = pd.to_datetime(statementDF.Date)

# filter out the days from the statement
statementDF.loc[(statementDF['Date'] > start_date) & (statementDF['Date'] <= end_date)]

# filter out income from paychecks
statementDF.loc[statementDF['Category'] == 'Paycheck']