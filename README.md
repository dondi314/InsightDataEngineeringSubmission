# InsightDataEngineeringSubmission
This is my submission to the Insight Data Engineering Coding Challenge.


The features in my submission are described below: 

### Feature 1: 
List the top 10 most active host/IP addresses that have accessed the site.

### Feature 2: 
Identify the 10 resources that consume the most bandwidth on the site

### Feature 3:
List the top 10 busiest (or most frequently visited) 60-minute periods 

### Feature 4: 
Detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes. Log those possible security breaches.

### Feature 5:
List the 10 users who consume the most bandwidth on the site.  For our purposes, bandwidth is measured as total bytes used by the user.

### Feature 6:
List all nonzero quarter hour time blocks in which the website received the most web traffic.

### Note, I have modified the run.sh file and the run_test.sh file to run my features
If you have trouble running my features, be sure to look at my run files

### A note on Feature 3 and 6
Feature 4 was the hardest feature to implement, and I believe the other features to be much more effective at running through large amounts of data in a short amount of time.  I also that Feature 3 was not very useful as worded.  With a website like NASA, which will see a lot of internet traffic, we probably need a better way of measuring the top 10 busiest 60-minute periods.  If subway hired you to determine the 3 busiest times of the day, and you told him 5:00:00pm, 5:00:01pm, and 5:00:002pm, you probably missed the point of his question.  This is why I implemented my own Feature 6 which runs very much faster.  Feature 6 measures the busiest 15 minute intervals on the quarter hour.  I am also averaging across days for this purpose.

Feature 3 runs after everything else runs.  If you want to see how the other features of my program run with respect to larger data, you can hastag out the very last line of the process_log.py file (i.e. feature_3(log_txt, hours_txt)), and the rest of the file should still run (other than failing test 3 each time).

## Details of my Implementation
I believe most of the packages I used were pretty standard.  The packages I used were itertools, operator, re, and datetime.  I have broken my file up into smaller pieces as you will see.  Everything should execute fine with the run file.

I programmed this on a Linux operating system (Ubuntu 16.04).  I believe this should work on a mac as well.

