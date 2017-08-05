#Downloads teacher data for each year and subject for both the district and the state

#url = 'http://profiles.doe.mass.edu/state_report/teacherdata.aspx?fycode=2015&export_excel=yes&subjectCode=42&reportType=SCHOOL'

#file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(2015) + '.xlsx'

import urllib.request

years = range(2008,2016)

subjects = {'Core':'12', 'ELA':'05', 'Geo':'07', 'Hist':'06', 'Math':'08', 'Reading':'04', 'Science':'13','SS':'11','Foreign Language':'02'}

for year in years:

    for subject, subject_id in subjects.items():
        
        url = 'http://profiles.doe.mass.edu/state_report/teacherdata.aspx?fycode=' + str(year) + '&export_excel=yes&subjectCode=' + subject_id + '&reportType=SCHOOL'

        file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(year) + '_' + subject + '.xls'
    
        urllib.request.urlretrieve(url,file_loc)


years2 = range(2005, 2016)

for year in years2:
        
    url = 'http://profiles.doe.mass.edu/state_report/teacherdata.aspx?fycode=' + str(year) + '&export_excel=yes&subjectCode=42&reportType=SCHOOL'

    file_loc = '/Users/taranraghuram/Documents/Project Euler/MA/Teacher Data' + '/' + str(year) + '_All.xls'
    
    urllib.request.urlretrieve(url,file_loc)

