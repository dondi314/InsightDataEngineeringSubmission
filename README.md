# Insight Data Engineering Submission
This is my submission to the Insight Data Engineering Coding Challenge.


The features in my submission are described below: 

### Feature 1: 
List the top 10 most active host/IP addresses that have accessed the site.

### Feature 2: 
Identify the 10 resources that consume the most bandwidth on the site.

### Feature 3:
List the top 10 busiest (or most frequently visited) 60-minute periods of time.

### Feature 4: 
Detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes. Log those possible security breaches.

### Feature 5:
List the 10 users who consume the most bandwidth on the site.  For our purposes, bandwidth is measured as total bytes used by the user.

### Feature 6:
List all busiest nonzero quarter hour time blocks of the week in order of web traffic received by the website from highest to lowest (take day of the week into account).

### Feature 7:
List all nonzero quarter hour time blocks of the week in order of web traffic received by the website from highest to lowest in terms of bandwidth (total number of bytes for our purposes).  Take the day of the week into account.

## About Feature 5, 6, and 7

### Feature 5 
List in descending order the top 10 most active hosts/IP addresses that have accessed the site.

Write to a file, named `top_ten_users_bandwidth.txt`, the 10 most active hosts/IP addresses in descending order in terms of bandwidth usage and (total bytes they have consumed).  There should be at most 10 lines in the file, and each line should include the host (or IP address) followed by a comma, and then the number of times it accessed the site. 

e.g., `top_ten_users_bandwidth.txt`:

    example.host.com,1000000
    another.example.net,800000
    31.41.59.26,600000
    
### Feature 6
List in descending order the site’s busiest (i.e. most frequently visited) 15-minute periods.

Write to a file named `busiest_quarter_hours.txt`, the hour of each 15-minute window follwed by 00, 15, 30, or 45, followed by the day of the week, followed by the number of times the site was accessed during that time period. The file should contain as many lines as nonzero entries (i.e. up to but no more than 24*4*7), with each line containing the start of each 15-minute window, followed by a comma and then the number of times the site was accessed during those 60 minutes. The lines should be listed in descending order with the busiest 60-minute window shown first. 

e.g., `hours.txt`:

    12:30 PM, Thursday,100
    11:00 AM, Wednesday,65
    02:00 PM, Tuesday,10
    01:00 AM, Saturday,8

I have included my file from the run of the large log.txt file.  My results are pretty interesting.  You get weekdays and middle of the day hours showing up at the top, and more weekend days and later hours showing up at the bottom of the list.  ...though I am a bit uncertain what to make of the hours because of timezones.

### Feature 7
List in descending order the site’s busiest (i.e. most frequently visited) 15-minute periods in terms of bandwidth.

Write to a file named `busiest_15_minute_bandwidth.txt`, the hour of each 15-minute window follwed by 00, 15, 30, or 45, followed by the day of the week, followed by the number of bytes occuring during that time period. The file should contain as many lines as nonzero entries (i.e. up to but no more than 24*4*7), with each line containing the start of each 15-minute window, followed by a comma and then the number of bytes occuring. The lines should be listed in descending order with the busiest 60-minute window shown first. 

e.g., `hours.txt`:

    12:30 PM, Thursday,100000
    11:00 AM, Wednesday,6505
    02:00 PM, Tuesday,1078
    01:00 AM, Saturday,89


### Note, I have modified the run.sh file and the run_test.sh file to run my features
If you have trouble running my features, be sure to look at my run files.

### A note on Feature 3 and 6
Feature 3 was the hardest feature to implement, and I believe the other features to be much more effective at running through large amounts of data in a short amount of time.  I also feel that Feature 3 was not very useful as worded.  With a website like NASA, which will see a lot of internet traffic, we probably need a better way of measuring the top 10 busiest 60-minute periods.  If the Subway CEO hired you to determine the 3 busiest times of the day at Subway restuarants, and you told him 5:00:00pm, 5:00:01pm, and 5:00:02pm, you probably missed the point of his question.  This is why I implemented my own Feature 6 which runs very much faster.  Feature 6 measures the busiest 15 minute intervals on the quarter hour.  I am also averaging across days for this purpose.

Feature 3 runs after everything else runs.  If you want to see how the other features of my program run with respect to larger data, you can hashtag out the very last line of the process_log.py file (i.e. feature_3(log_txt, hours_txt)), and the rest of the file should still run (other than failing test 3 each time).

## Details of my Implementation
I believe most of the packages I used were pretty standard.  The packages I used were itertools, operator, re, datetime, and calendar.  I have broken my file up into smaller pieces as you will see.  Everything should execute fine with the run file.

I programmed this on a Linux operating system (Ubuntu 16.04).  I believe this should work on a mac as well.

