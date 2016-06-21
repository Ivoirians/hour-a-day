import datetime, os, shutil, sys

startDay = datetime.date(year=2016, month=6, day=19)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    days = str((datetime.datetime.now().date() - startDay).days)
    if len(argv) > 1:
        days = argv[1]
    if os.path.exists(days):
        print "Day already generated"
        return
    print "Starting day " + days
    os.mkdir(str(days))
    with open("bare_template.html", 'r') as template:
        src = template.read()
        src = src.replace('{today}', days)
        print src
        with open("{0}/{0}.html".format(days), 'w') as dest:
            dest.write(src)
    with open("index.html", 'a') as indexFile:
        indexFile.write("<br><a href=\"{0}/{0}.html\">{0}</a>\n".format(days))
    try:
        shutil.copyfile("{0}/{0}.css".format(int(days) - 1), "{0}/{0}.css".format(days))
    except ValueError:
        print ("Filename was not a number. Cannot fetch incremental CSS file.")
main()

