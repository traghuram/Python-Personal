
import urllib.request

url = 'http://profiles.doe.mass.edu/state_report/teacherdata.aspx?fycode=2015&export_excel=yes&subjectCode=42&reportType=SCHOOL'

testfile = urllib.request.urlopen(url)

#testfile.retrieve(url, "test.xslx")
