#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=AL:AL'
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=HN:Y
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=SS:LEP
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=FL:Y
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=SS:SPED
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:02
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:01
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:03
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:04
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:06
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:20
#http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohortYear=2014&reportType=DISTRICT&rateType=4-Year:REG&studentGroup=RA1:15

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(2015) + '.xlsx'

import urllib.request

years = range(2008,2015)

jurisdictions = ['SCHOOL', 'DISTRICT']

functions = {'All':'AL:AL', 'High Needs':'HN:Y', 'ELL':'SS:LEP', 'FRL':'FL:Y', 'SPED':'SS:SPED', 'PD':'8', 'Black':'RA1:02','Native American':'RA1:01',
             'Asian':'RA1:03', 'Latino':'RA1:04', 'Multi-race':'RA1:06', 'Pacific Islander':'RA1:20', 'White':'RA1:15'}

for year in years:

    for jurisdiction in jurisdictions:

        for function, function_id in functions.items():
            
            url = 'http://profiles.doe.mass.edu/state_report/mobilityrates.aspx?&export_excel=yes&cohort' + str(year) + '&reportType=' + jurisdiction + '&rateType=4-Year:REG&studentGroup=' + function_id

            file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Student Mobility' + '/' + str(year) + '_' + function + '_' + jurisdiction + '.xls'
        
            urllib.request.urlretrieve(url,file_loc)
