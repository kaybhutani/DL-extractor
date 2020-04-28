import os

# enter your test data here
# format [ [licenseNo, DOB], [licenseNo, DOB], [licenseNo, DOB] ...]

testData = [
  ["DL0420110149646", "09-02-1976"],
  ["DL420180001387", "25-03-1999"]
]

for testCase in testData:
  os.system("python main.py -l {} -d{} -o{}".format(testCase[0], testCase[1], "test/" + testCase[0]) + ".json")