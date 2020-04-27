from getData import getData

response = getData(licenseNo = licenseNo, dob = dob).scrapeData()

if response:
  print(response)
