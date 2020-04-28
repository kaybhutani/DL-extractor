from getData import getData
# self creaeted package getData.py
import argparse
import json

initialhelpMessage = "To get Details of a Driver, Enter DL Number using -l, Enter DOB using -d. \nExample Command: python main.py -l \"DL0420110149646\" -d \"09-02-1976\""

parser = argparse.ArgumentParser(description=initialhelpMessage)
parser.add_argument('--licenseNo', '-l', required=True, help='License Number of your Driving License. Please enter it without any special characters')
parser.add_argument('--dob', '-d', required=True, help='Date of Birth as on Driving License. (dd-mm-yyyy)')
parser.add_argument('--output', '-o', required=False, default="DriverData.json", help='Output File name. Default is DriverData.json')
args = parser.parse_args()

licenseNo = args.licenseNo
dob = args.dob
outputFile = args.output

response = getData(licenseNo = licenseNo, dob = dob).scrapeData()
if response:
  with open(outputFile, 'w') as output:
    json.dump(response, output)
    print("Driver Details Successfully stored in ", outputFile)
