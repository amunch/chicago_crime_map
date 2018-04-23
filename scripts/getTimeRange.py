import sys

startyear = 2018
startmonth = 3
endyear = 2018
endmonth = 4

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        exit(1)
    count = 0
    firstline = True
    with open(sys.argv[1]) as f:
        outputfilename = "output"+str(startmonth)+"_"+str(startyear)+"-"+str(endmonth)+"_"+str(endyear)+".csv"
        with open(outputfilename,'w+') as outputfile:
            for line in f:
                if firstline:
                    firstline = False
                    outputfile.write(line)
                    continue
                linestrip = line.rstrip()
                commasplit = linestrip.split(',')
                dateobject = commasplit[1]
                dateobject = dateobject.split(' ')[0] # get just date
                dateobject = dateobject.split('/')
                #print(dateobject)
                if int(dateobject[2]) >= startyear and int(dateobject[2]) <= endyear:
                    if startyear == endyear:
                        if int(dateobject[0]) >= startmonth and int(dateobject[0]) <= endmonth:
                            # just add it
                            count = count + 1
                            outputfile.write(line)
                    else:
                        if int(dateobject[2]) != startyear and int(dateobject[2]) != endyear:
                            # just add it
                            count = count + 1
                            outputfile.write(line)
                        elif int(dateobject[2]) == startyear:
                            if int(dateobject[0]) >= startmonth:
                                # just add it
                                count = count + 1
                                outputfile.write(line)
                        else:
                            if int(dateobject[0]) <= endmonth:
                                # just add it
                                count = count + 1
                                outputfile.write(line)
    print(str(count))