import requests
from bs4 import BeautifulSoup
from extractData import extractData
url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'

class getData:
  def __init__(self, licenseNo, dob):
    self.licenseNo = licenseNo
    self.dob = dob

  def authentiCate(self, soupData):
    if (soupData.find('No DL Details Found....') == -1): #this message is showed only when details are wrong
      return False
    return True

  def scrapeData(self):
    formData = {
          'javax.faces.partial.ajax': 'true',
          'javax.faces.source': 'form_rcdl:j_idt46',
          'javax.faces.partial.execute': '@all',
          'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
          'form_rcdl:j_idt46': 'form_rcdl:j_idt46',
          'form_rcdl': 'form_rcdl',
          'form_rcdl:tf_dlNO': self.licenseNo,
          'form_rcdl:tf_dob_input': self.dob
      }
    session = requests.Session()
    pageData = session.get(url)
    soup = BeautifulSoup(pageData.content, features= 'lxml')
    viewStateCode = soup.find('input', attrs = {'name': 'javax.faces.ViewState'})['value']
    formData['javax.faces.ViewState'] = viewStateCode #viewState code is unique everytime, get new from each session
    response = session.post(url, data = formData) #request works without captcha, get_captcha() not needed
    responseData = BeautifulSoup(response.text, features='lxml')
    authentication = self.authentiCate(responseData)
    if authentication:  
      try:
        tableList = responseData.find_all('table')
        jsonData = extractData(tableList).getJSON()
        return jsonData
      except Exception as error:
        print("Some error occurred while fetching data, please report at yourCompany@Email.com")
        return False
    else:
      return False
