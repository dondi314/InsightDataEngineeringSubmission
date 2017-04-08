touch cow.txt
rm *cow.txt*
split --lines=36000 --numeric-suffixes --suffix-length=4 log.txt cow.txt
cd data
touch hours.txt
cd ..
python ./parallel_compute_hours.py
rm *cow.txt*
split --lines=30000 --numeric-suffixes --suffix-length=4 log.txt cow.txt
cd data
cp hours.txt hours1.txt
cd ..
python ./parallel_compute_hours.py
python ./compare_lists.py
rm *cow.txt*
