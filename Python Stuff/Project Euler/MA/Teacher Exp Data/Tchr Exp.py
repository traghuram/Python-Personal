#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/agestaffing.aspx?ctl00$ContentPlaceHolder1$fycode=2015&export_excel=yes&ctl00$ContentPlaceHolder1$displayType=NUM&ctl00$ContentPlaceHolder1$jobClass=4100&ctl00$ContentPlaceHolder1$reportType=SCHOOL'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(2015) + '.xlsx'

import urllib.request

years = range(2008,2016)

jobs = {'All':'1100', 'Superintendent':'1200', 'Asst Sup':'1201', 'School Business Official':'1202', 'Other District-wide admins':'1205', 'Principal or Head of School':'1305',
        'Asst Principal':'1310','Teacher':'2305','Co Teachers':'2306', 'Long-Term Sub':'2325', 'Paras':'4100'}

for year in years:

    for job, job_id in jobs.items():
        
        url = 'http://profiles.doe.mass.edu/state_report/agestaffing.aspx?ctl00$ContentPlaceHolder1$fycode=' + str(year) + '&export_excel=yes&ctl00$ContentPlaceHolder1$displayType=NUM&ctl00$ContentPlaceHolder1$jobClass=' + job_id + '&ctl00$ContentPlaceHolder1$reportType=SCHOOL'

        file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Exp Data' + '/' + str(year) + '_' + job + '.xls'
    
        urllib.request.urlretrieve(url,file_loc)

