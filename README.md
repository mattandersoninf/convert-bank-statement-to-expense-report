# Convert Bank Statement To Expense Report


This project aims to convert bank statements (csv) into google sheets expense reports.

At this time, this project leverages the Google Sheets Monthly Budget template.

# Dependencies
[Google Drive v3 API Docs](https://developers.google.com/drive/api/v3/reference/)
[pdftotext](https://pypi.org/project/pdftotext/)

# Information

client_secret.json format
- gmail: user gmail address
- password: password to google account
- stament_filepath: local bank statement csv filepath
- budget_filepath: local budget xlsx filepath
(ignore client id and client service for now)
  
# To-Do List: 

Read in data from statement / sheet / etc
- [x] Exception handle for file not found 
- [x] Modify data locally
- [ ] Save copy locally
- [ ] Exception handle for saving copy locally
- [ ] (Complete the above steps then have the program overwrite the expense report if a report of the same name already exists in oyour directory)
  
Upload data to Drive / Format into two monthly sheets (graphs , )
- [x] Connect to drive account
- [ ] Exception handle for being unable to connect
- [ ] Upload to drive
- [ ] Exception handle for connection / upload failure
- [ ] Programmatically copy template into XXXXmonth_budget_sheet
- [ ] Exception handle for the case when template does not exist (exit program)
- [ ] Exception handle for not being able to copy
- [ ] Fill in the information to (above)
- [ ] Exception handle for not being able to fill in the information 

Stretch Goal: Read from Bank PDF Statements
- [ ] Option 1: Read from bank statement (PDF)
- [ ] Option 2: Mint (app that connects to bank and tracks spending for you)
  NOTE: Mint API is relatively forgiving
- [ ] Option 3: Read from bank APIs (WARNING: banks don't allow access to APIs easily)

Other Ideas:
- [ ] Migrate To-Do list to GitHub Issue tracking
- [ ] (Maybe?) migrate GitHub repository to GitLab project
- [ ] (Maybe?) consider making a front end for this (sheets is fine for now)
- [ ] Web app with user authentication, file uploads, charts

# Known Issues
During installation, it is known that installing pdftotext can cause some issues. There are known solutions at the following links:
[Stackoverflow](https://stackoverflow.com/a/58139729)
[Coder.Haus's Personal Blog](https://coder.haus/2019/09/27/installing-pdftotext-through-pip-on-windows-10/)
[Conda Install](https://anaconda.org/conda-

