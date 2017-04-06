# -*- coding: utf-8 -*-
from datetime import datetime
import re

def convertdatetimeobject(input):
    dictionary_month = {}
    dictionary_month[1] = 'Jan'
    dictionary_month[2] = 'Feb'
    dictionary_month[3] = 'Mar'
    dictionary_month[4] = 'Apr'
    dictionary_month[5] = 'May'
    dictionary_month[6] = 'Jun'
    dictionary_month[7] = 'Jul'
    dictionary_month[8] = 'Aug'
    dictionary_month[9] = 'Sep'
    dictionary_month[10] = 'Oct'
    dictionary_month[11] = 'Nov'
    dictionary_month[12] = 'Dec'
    month = dictionary_month[input.month]
    day = input.day
    year = input.year
    minute = input.minute
    hour = input.hour
    second = input.second
    if second < 10:
        second = '0%d'%second
    else:
        second = '%d'%second
    if hour < 10:
        hour = '0%d'%hour
    else:
        hour = '%d'%hour
    if day < 10:
        day = '0%d'%day
    else:
        day = '%d'%day
    if minute < 10:
        minute = '0%d'%minute
    else:
        minute = '%d'%minute

    string = day+'/'+month+'/'+'%d'%year+':'+hour+':'+minute+':'+second+' -0400'
    return string

def mytimestamp(date):
    cleandate = date.split()
    cleandate1 = cleandate[0].replace("/"," ").replace(":", " ").split()
    year = cleandate1[2]
    month = cleandate1[1].replace(".", "").lower()
    day = cleandate1[0]
    hour = cleandate1[3]
    minute = cleandate1[4]
    second = cleandate1[5]
    dictionary_month = {}
    dictionary_month['jan'] = 1
    dictionary_month['january'] = 1
    dictionary_month['feb'] = 2
    dictionary_month['february'] = 2
    dictionary_month['mar'] = 3
    dictionary_month['march'] = 3
    dictionary_month['apr'] = 4
    dictionary_month['april'] = 4
    dictionary_month['may'] = 5
    dictionary_month['jun'] = 6
    dictionary_month['june'] = 6
    dictionary_month['jul'] = 7
    dictionary_month['july'] = 7
    dictionary_month['aug'] = 8
    dictionary_month['august'] = 9
    dictionary_month['sep'] = 9
    dictionary_month['sept'] = 9
    dictionary_month['septem'] = 9
    dictionary_month['september'] = 9
    dictionary_month['oct'] = 10
    dictionary_month['october'] = 10
    dictionary_month['nov'] = 11
    dictionary_month['novem'] = 11
    dictionary_month['november'] = 11
    dictionary_month['dec'] = 12
    dictionary_month['december'] = 12
    digit_minute = (int(minute[0])*10)+int(minute[1])
    digit_hour = (int(hour[0])*10)+int(hour[1])
    digit_second = (int(second[0])*10)+int(second[1])
    digit_day = (int(day[0])*10)+int(day[1])
    month_number = dictionary_month[month]
    digit_year = (int(year[0])*(10**3))+(int(year[1])*(10**2))+(int(year[2])*(10))+int(year[3])
    since = datetime( 1970, 1, 11, 0, 0, 0 )
    mytime = datetime( digit_year, month_number, digit_day, digit_hour, digit_minute, digit_second )
    return mytime


def resource(word):
    word = word.replace('-0400','            ').replace('HTTP/1.0', '         ').replace('- -', '               ')
    r = re.compile(r"[^a-zA-Z0-9/.:_!@#$%,:?]")
    newword = r.sub(' ', word).strip()
    newword = re.split(r'\s{5,}', newword)
    my_resource = newword[2].split()[1::]
    string = ''.join(my_resource)
    return string

def timestamp(word):
    time = " ".join(word.replace(']', '').replace('- -', '').replace('[', '').split()).split()[1]
    return str(time)
def date_seconds(date):
    cleandate = date.split()
    cleandate1 = cleandate[0].replace("/"," ").replace(":", " ").split()
    year = cleandate1[2]
    month = cleandate1[1].replace(".", "").lower()
    day = cleandate1[0]
    hour = cleandate1[3]
    minute = cleandate1[4]
    second = cleandate1[5]
    dictionary_month = {}
    dictionary_month['jan'] = 1
    dictionary_month['january'] = 1
    dictionary_month['feb'] = 2
    dictionary_month['february'] = 2
    dictionary_month['mar'] = 3
    dictionary_month['march'] = 3
    dictionary_month['apr'] = 4
    dictionary_month['april'] = 4
    dictionary_month['may'] = 5
    dictionary_month['jun'] = 6
    dictionary_month['june'] = 6
    dictionary_month['jul'] = 7
    dictionary_month['july'] = 7
    dictionary_month['aug'] = 8
    dictionary_month['august'] = 9
    dictionary_month['sep'] = 9
    dictionary_month['sept'] = 9
    dictionary_month['septem'] = 9
    dictionary_month['september'] = 9
    dictionary_month['oct'] = 10
    dictionary_month['october'] = 10
    dictionary_month['nov'] = 11
    dictionary_month['novem'] = 11
    dictionary_month['november'] = 11
    dictionary_month['dec'] = 12
    dictionary_month['december'] = 12
    digit_minute = (int(minute[0])*10)+int(minute[1])
    digit_hour = (int(hour[0])*10)+int(hour[1])
    digit_second = (int(second[0])*10)+int(second[1])
    digit_day = (int(day[0])*10)+int(day[1])
    month_number = dictionary_month[month]
    digit_year = (int(year[0])*(10**3))+(int(year[1])*(10**2))+(int(year[2])*(10))+int(year[3])
    since = datetime( 1970, 1, 11, 0, 0, 0 )
    mytime = datetime( digit_year, month_number, digit_day, digit_hour, digit_minute, digit_second )
    diff_seconds = int((mytime-since).total_seconds())
    return diff_seconds

def code_bits(input):
    input = input.replace('-0400','            ').replace('HTTP/1.0', '         ').replace('- -', '               ')
    word = input.replace('-', '0')
    r = re.compile(r"[^a-zA-Z0-9/.:_]")
    newword = r.sub(' ', word).strip()
    newword = re.split(r'\s{5,}', newword)
    Len = len(newword)
    codebits = newword[Len-1].split()
    if len(codebits) == 2:
        code = codebits[0]
        digbits = 0
        bits = codebits[1]
        L_B = len(bits)
        revbits = bits[::-1]
        for i in range(0, L_B):
            digbits += int(revbits[i])*(10**i)
    else:
        digbits = 0
        code = ''.join(codebits)
    return code, digbits

def security_breach(code):
    if code == '401':
        return True


def ipaddress(input):
    ip = "".join((input.split("- -"))[0])
    return ip



def how_to_convert(input):
    day = {}

    day[6] = 'Sunday'
    day[0] = 'Monday'
    day[1] = 'Tuesday'
    day[2] = 'Wednesday'
    day[3] = 'Thursday'
    day[4] = 'Friday'
    day[5] = 'Saturday'

    quarter = {}

    quarter[0] = '00'
    quarter[1] = '15'
    quarter[2] = '30'
    quarter[3] = '45'

    hour = {}

    hour[0] = ['12', 'AM']
    hour[1] = ['01', 'AM']
    hour[2] = ['02', 'AM']
    hour[3] = ['03', 'AM']
    hour[4] = ['04', 'AM']
    hour[5] = ['05', 'AM']
    hour[6] = ['06', 'AM']
    hour[7] = ['07', 'AM']
    hour[8] = ['08', 'AM']
    hour[9] = ['09', 'AM']
    hour[10] = ['10', 'AM']
    hour[11] = ['11', 'AM']
    hour[12] = ['12', 'PM']
    hour[13] = ['01', 'PM']
    hour[14] = ['02', 'PM']
    hour[15] = ['03', 'PM']
    hour[16] = ['04', 'PM']
    hour[17] = ['05', 'PM']
    hour[18] = ['06', 'PM']
    hour[19] = ['07', 'PM']
    hour[20] = ['08', 'PM']
    hour[21] = ['09', 'PM']
    hour[22] = ['10', 'PM']
    hour[23] = ['11', 'PM']

    string = hour[input[0]][0]+':'+quarter[input[1]]+' '+hour[input[0]][1]+', '+ day[input[2]]
    return string
