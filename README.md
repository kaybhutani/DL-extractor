# Driving License Extractor

This project fetches Driving License details from https://parivahan.gov.in using DL number.

## Setting up project

To set up virtual environment use

`virtualenv .venv`

and activate it by doing

`source .venv/bin/activate`

To install the dependencies do:- 

`pip install requirements.txt`


## To get Driver Details

Run `python main.py -l LICENSE_NO -d DOB -o OUTPUT_FILE.JSON`

In above command, LICENSE_NO is the Driver License Number you want to get the details for, DOB is date of birth in dd-mm-yyyy format. and OUTPUT_FILE.json is the name of output file (This is optional)

Example: `python main.py -l DL1234567891234 -d 01-01-2000`

## To Test Multiple DL at once

To test multiple DL at once, append the DL number and DOB in `testData` in `test.py` file (as in the givent format)

Make sure there is a `test` folder created to store all the files.

Once done, you can run `python test.py` to check multiple DL at once.