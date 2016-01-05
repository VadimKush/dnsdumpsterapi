import re
import StringIO
import warnings
import openpyxl
from requests import get,post

class DNSdumpster():
	def __init__(self,domain):
		warnings.filterwarnings('ignore')
		self.sub_regex = re.compile("([a-zA-Z0-9][a-zA-Z0-9.-]+[a-zA-Z0-9])")
		self.domain = str(domain)
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/40.0','Referer': 'https://dnsdumpster.com'}
		self.url = "https://dnsdumpster.com"
		self.cookie = {"csrftoken":"MJatUeBIe1HwtfEpIJd61WmbznSpScPg"}
		self.postdata = {"csrfmiddlewaretoken":"MJatUeBIe1HwtfEpIJd61WmbznSpScPg","targetip":self.domain}
		self.xlsx = ""
		self.subdomains = []
	def get_data(self):
		page = post(url=self.url,data=self.postdata,cookies=self.cookie,headers=self.headers).content
		regex = re.compile("<a href=\"(https:\/\/dnsdumpster\.com\/static\/xls\/.+?\.xlsx)\">")
		url = regex.findall(page)[0]
		self.xlsx = get(url).content
	def analyze_data(self):
		a=StringIO.StringIO()
		a.write(self.xlsx)
		data = openpyxl.load_workbook(a)
		sheet = data.get_sheet_by_name("All Hosts")
		tmp=list()
		i=2
		while(True):
			if(sheet["C"+str(i)].value == None):
				break
			if(sheet["C"+str(i)].value == "A" or sheet["C"+str(i)].value == "MX"):
				tmp.append(self.sub_regex.findall(sheet["A"+str(i)].value)[0])
			i+=1
		self.subdomains = self.uniqify(tmp)
	def uniqify(self,dlist,idfun=None):
		if idfun is None:
			def idfun(x):
				return x
		seen = {}
		result = []
		for item in dlist:
			marker = idfun(item)
			if marker in seen: continue
			seen[marker] = 1
			result.append(item)
		return result
	def get_subdomains(self):
		self.get_data()
		self.analyze_data()
		return self.subdomains