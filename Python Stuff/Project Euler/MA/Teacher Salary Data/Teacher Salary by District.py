#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/teachersalaries.aspx?mode=&orderBy=&year=2012&filterBy=&export_excel=yes'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(2015) + '.xls'

import urllib.request

years = range(1997,2014)

for year in years:
        
    url = 'http://profiles.doe.mass.edu/state_report/teachersalaries.aspx?mode=&orderBy=&year=' + str(year) + '&filterBy=&export_excel=yes'
        
    file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Salary Data' + '/' + str(year) + '.xls'
    
    urllib.request.urlretrieve(url,file_loc)

