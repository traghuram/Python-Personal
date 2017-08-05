#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/staffingRetentionRates.aspx?ctl00$ContentPlaceHolder1$fycode=2014&export_excel=yes&ctl00$ContentPlaceHolder1$reportType=DISTRICT'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Enrollment' + '/' + str(2015) + '.xls'

import urllib.request

years = range(2008,2015)

domains = ['SCHOOL', 'DISTRICT']

for year in years:
    
        for domain in domains:
            
            url = 'http://profiles.doe.mass.edu/state_report/staffingRetentionRates.aspx?ctl00$ContentPlaceHolder1$fycode=' + str(year) + '&export_excel=yes&ctl00$ContentPlaceHolder1$reportType=' + domain
        
            file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Retention' + '/' + str(year) + '_' + domain + '.xls'
    
            urllib.request.urlretrieve(url,file_loc)

            #print(year, domain)

