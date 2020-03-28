"""
route /accounts/add_data aufrufen um user zu generieren
muss in urls.py auskommentiert werden
"""
import numpy as np
import uuid, json
from datetime import datetime, timedelta
import random
import csv

# plzs = {}
# with open("../mapview/files/CH.csv", encoding='utf-8') as csvfile:
#   reader = csv.DictReader(csvfile, fieldnames=["plz","lat","lon","ort"])
#   next(csvfile)
#   for row in reader:
#       plzs[row["plz"]] = (float(row["lon"]), float(row["lat"]), row["ort"])

from apps.ineedstudent.models import Hospital
from apps.iamstudent.models import Student, AUSBILDUNGS_TYPEN_COLUMNS
from apps.accounts.models import User
from django.http import HttpResponse

mail = lambda x: '%s@email.com' % x
big_city_plzs = ['8000','8400','1200','4000','3000','6000','7000','1000','9000','6900','8200','8500',]

# def random_plz():
#     return random.choice(list(plzs.keys()))

def big_city_plz():
    return random.choice(big_city_plzs)

def delete_fakes():
    User.objects.filter(email__contains='email').delete()


def populate_db(request):
    delete_fakes()
    n_student = 200
    n_hospital = 20
    #plzs = np.random.choice(big_city_plzs, size=n_student)
    months = np.random.choice(np.arange(1,12),size=n_student)
    days = np.random.choice(np.arange(2,15),size=n_student)
    year = 2020

    for i in range(n_student):
        idx = i
        m = mail(i)
        kwd = dict(zip(AUSBILDUNGS_TYPEN_COLUMNS,np.random.choice([True,False],size=len(AUSBILDUNGS_TYPEN_COLUMNS))))
        random_time = (datetime.now() - timedelta(days=random.randint(0,40), hours=random.randint(0,23), minutes=random.randint(0,59))).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:-3] + 'Z'
        pwd = User.objects.make_random_password()
        u = User.objects.create(username=m, email=m, is_student=True, password=pwd)
        s = Student.objects.create(user=u,
                                   plz=big_city_plz(),
                                   availability_start='{}-{:02d}-{:02d}'.format(year,months[i],days[i]),
                                   uuid=str(uuid.uuid4()),
                                   registration_date=random_time,
                                   **kwd
                                   )
                                                                      
    plzs = np.random.choice(big_city_plzs, size=n_student)
    for i in range(n_hospital):
        m = mail(i+n_student)
        random_time = (datetime.now() - timedelta(days=random.randint(0,40), hours=random.randint(0,23), minutes=random.randint(0,59))).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:-3] + 'Z'
        pwd = User.objects.make_random_password()
        u = User.objects.create(username=m, email=m, is_student=True, password=pwd)
        s = Hospital.objects.create(user=u,
                                    plz=big_city_plz(),
                                    ansprechpartner='XY',
                                    sonstige_infos='yeaah',
                                    uuid=str(uuid.uuid4()),
                                    registration_date=random_time,
                                   )


    return HttpResponse('Done. %s entries.' % User.objects.all().count())
