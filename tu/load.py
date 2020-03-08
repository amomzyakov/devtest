import csv
import tu.wsgi
from main import models
from datetime import datetime

fname = 'data.csv'

with open(fname) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        reg = models.Region.objects.filter(name=row['region'])
        cnt = reg.count()
        if cnt == 1:
            reg = reg[0]
        if cnt == 0:
            reg = models.Region(name=row['region'])
            reg.save()
        contractor = models.Contractor.objects.filter(name=row['contractor'])
        cnt = contractor.count()
        if cnt == 1:
            contractor = contractor[0]
        if cnt == 0:
            contractor = models.Contractor(name=row['contractor'])
            contractor.save()
        appl_date = datetime.strptime(row['appl_date'], '%d.%m.%Y').date()
        resp_date = None
        if row['resp_date']:
            resp_date = datetime.strptime(row['resp_date'], '%d.%m.%Y').date()
        print(row['applnum'], appl_date, resp_date)
        appl = models.Appl(applnum=row['applnum'],
                            sitenum=row['sitenum'],
                            region=reg,
                            contractor=contractor,
                            appl_date=appl_date,
                            resp_date=resp_date,
                            resolution=row['resolution']
                           )
        appl.save()


