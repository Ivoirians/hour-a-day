import datetime, os, shutil, sys

startDay = datetime.date(year=2016, month=6, day=19)

def main(argv=None):
	if argv is None:
		argv = sys.argv
	days = str((datetime.datetime.now().date() - startDay).days)
	if len(argv) > 1:
		days = argv[1]
	if os.path.exists(str(days)):
		print "Day already generated"
		return
	os.mkdir(str(days))
	with open("bare_template.html", 'r') as template:
		src = template.read()
		src.replace('{today}', str(days))
		with open("{0}/{0}.html".format(days), 'w') as dest:
			dest.write(src)

	shutil.copyfile("{0}/{0}.css".format(int(days) - 1), "{0}/{0}.css".format(days))

main()

