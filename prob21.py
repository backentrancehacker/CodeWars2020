#solves problem 21
'''
You will receive the data from the timeclock application in the format of:
EMPLOYEE NAME (string)
RATE ##.## (double)
IN #### (int)
OUT #### (int)
IN #### (int)
OUT #### (int)
'''

'''
Run the calculations for each employee's day and output the amount they earned by multiplying the time they
worked by their hourly rate. Use the employee's name, and format their day's earnings into the format of $#.00
(rounded to 2 decimal places)

EMPLOYEE JANE
RATE 12.00
IN 0800
OUT 1200
IN 1230
OUT 1630
EMPLOYEE MIKE
RATE 09.99
IN 0917
OUT 1200
IN 1303
OUT 1700
EMPLOYEE MICHELLE
RATE 15.00
IN 0730
OUT 1200
IN 0000
OUT 0000

JANE earned $96.00
MIKE earned $66.60
MICHELLE earned $67.50
'''
import time
list1 = []
loopbreak = time.time() + 1
#timed loop with an exeption for the EOF error
try:
    while loopbreak > time.time():
        list1.append(input())
except EOFError:
    count = len(list1)
    count = count / 6
    count = int(count)
    for m in range(0, count):
        #gets rid of unessecary info such as EMPLOYEE, RATE, IN, and OUT
        p, name = list1[0 + (m * 6)].split()
        p, rate = list1[1 + (m * 6)].split()
        p, in1 = list1[2 + (m * 6)].split()
        p, out1 = list1[3 + (m * 6)].split()
        p, in2 = list1[4 + (m * 6)].split()
        p, out2 = list1[5 + (m * 6)].split()

        rate = float(rate)

        n = 2
        #splits each number in half in order to do conversion math
        in1, min1 = [in1[i:i+n] for i in range(0, len(in1), n)]
        out1, min2 = [out1[j:j+n] for j in range(0, len(out1), n)]
        in2, min3 = [in2[k:k+n] for k in range(0, len(in2), n)]
        out2, min4 = [out2[l:l+n] for l in range(0, len(out2), n)]
                #all of this becomes integer
        #these become two digit numbers
        in1 = int(in1)
        out1 = int(out1)
        in2 = int(in2)
        out2 = int(out2)
        #these become two digit numbers
        min1 = int(min1)
        min2 = int(min2)
        min3 = int(min3)
        min4 = int(min4)
        #divide by 60 to get decimal of minutes
        min1 = (min1/60)
        min2 = (min2/60)
        min3 = (min3/60)
        min4 = (min4/60)
        #adds the minute decimal to the hours
        #you now have a number like 12.37 that can be multiplied by a rate like 13.45
        in1 = in1 + min1
        out1 = out1 + min2
        in2 = in2 + min3
        out2 = out2 + min4
        #creates time blocks
        first = out1 - in1
        second = out2 - in2
        #adds time blocks and calculates wage
        time = first + second
        total = time * rate
        total = "{:.2f}".format(total)
        print(name, "earned $" + str(total))