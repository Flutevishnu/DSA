def timeConversion(s):
    # print(s.split(':')[2][2:])
    AM_PM = s.split(':')[2][2:]
    time = s.split(':')
    if AM_PM == "AM":
        if s.split(':')[0] == "12":
            time[0] = '00'
            temp = ''
            for i in time:
                temp+=i+":"
            return temp[:8]
        return s[:8]
    else:
        if s.split(':')[0] == "12":
            return s[:8]
        else:
           
            time[0] = str(int(s[0:2])+12)
            time[2] = time[2][0:2]
            temp = ""
            for i in time:
                temp+= i+":"
            # print(temp)
            return temp[:8]
        
print(timeConversion('12:40:22AM'))