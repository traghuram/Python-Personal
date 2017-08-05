#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/selectedpopulations.aspx?mode=school&year=2015&Continue.x=5&Continue.y=3&export_excel=yes'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(2015) + '.xls'

import urllib.request

years = range(1994,2016)

domains = ['school', 'district']

for year in years:
    
        for domain in domains:
            
            url = 'http://profiles.doe.mass.edu/state_report/selectedpopulations.aspx?mode=' + domain + '&year=' + str(year) + '&Continue.x=5&Continue.y=3&export_excel=yes'
        
            file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment by Sel Pop' + '/' + str(year) + '_' + domain + '.xls'
    
            urllib.request.urlretrieve(url,file_loc)

            #print(year, domain)

