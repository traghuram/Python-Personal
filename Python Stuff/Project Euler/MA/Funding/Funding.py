#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/ppx.aspx?&export_excel=yes&finFunction=14&year=2013'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(2015) + '.xlsx'

import urllib.request

years = range(2005,2014)

functions = {'Total':'17', 'Admin':'4', 'Instr Leadership':'5', 'Teachers':'6', 'Other Teaching':'7', 'PD':'8', 'Instructional Materials':'9','Guidance and Testing':'10',
             'Pupil Services':'11', 'O&M':'12', 'Insurance, Retirement, Other':'13', 'Outplaced Tuition':'14'}

for year in years:

    for function, function_id in functions.items():
        
        url = 'http://profiles.doe.mass.edu/state_report/ppx.aspx?&export_excel=yes&finFunction=' + function_id + '&year=' + str(year)

        file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Funding' + '/' + str(year) + '_' + function + '.xls'
    
        urllib.request.urlretrieve(url,file_loc)
