# Ideas from the gravyard

I have included a program that I never ended up finishing due to a lack of time.  The idea is that to figure out the maximum
hours, we can divide the log.txt file into small chunks and then claculate the max of each chunk.  I used 36000 lines in my bash script because that is ten times 3600 which is 10 times the number of seconds in an hour.  I now realize this number was too small.  Any way, as long as you choose a number bigger than a max (which presumably you could guess), then you will get the max as long as it isn't on the edge of one one of the text's chop off points.  But to make the results more accurate, you could run the program again in a different partition, and then see what answer you get.
