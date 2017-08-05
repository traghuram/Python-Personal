#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/gradesubjectstaffing.aspx?ctl00$ContentPlaceHolder1$fycode=2015&export_excel=yes&ctl00$ContentPlaceHolder1$displayType=NUM&ctl00$ContentPlaceHolder1$subjectCode=44&ctl00$ContentPlaceHolder1$reportType=SCHOOL'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(2015) + '.xls'

import urllib.request

years = range(2008,2016)

for year in years:
        
    url = 'http://profiles.doe.mass.edu/state_report/gradesubjectstaffing.aspx?ctl00$ContentPlaceHolder1$fycode=' + str(year) + '&export_excel=yes&ctl00$ContentPlaceHolder1$displayType=NUM&ctl00$ContentPlaceHolder1$subjectCode=44&ctl00$ContentPlaceHolder1$reportType=SCHOOL'
    
    file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher by Grade Data' + '/' + str(year) + '_bygrade.xls'
    
    urllib.request.urlretrieve(url,file_loc)

