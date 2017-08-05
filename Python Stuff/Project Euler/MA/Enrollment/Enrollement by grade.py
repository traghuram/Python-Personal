#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/enrollmentbygrade.aspx?mode=school&year=2015&Continue.x=6&Continue.y=0&export_excel=yes'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(2015) + '.xls'

import urllib.request

years = range(2008,2016)

for year in years:
        
    url = 'http://profiles.doe.mass.edu/state_report/enrollmentbygrade.aspx?mode=school&year=' + str(year) + '&Continue.x=6&Continue.y=0&export_excel=yes'

    file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(year) + '_bygrade.xls'
    
    urllib.request.urlretrieve(url,file_loc)

