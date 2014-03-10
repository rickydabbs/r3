import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "r3.settings")

from app.models import Prop

f = open('work1.txt', 'r')
contents = f.read()
lines = contents.split('\n')
for l in lines:
	shortname = l[2:7]
	address = l[7:37]
	city = l[37:52]
	state = l[52:54]
	zip = l[54:64]
	comment = l[124:164] + ' ' + l[164:204]
	enis_no = l[204:206]
	print(shortname, address, city, state, zip, comment, enis_no)
	p=Prop(
		short_name=shortname,
		address=address,
		city=city,
		state=state,
		zip=zip,
		comment=comment,
		enis_no=enis_no,
		mgmt_co='',
		mgmt_pct=0)
	p.save()
	
