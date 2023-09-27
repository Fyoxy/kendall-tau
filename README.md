# kendall-tau
Project for Exact Methods in Decision Processes class homework where we had to calculate Kendall-Tau distances for every student who had to rank pictures in pairwise comparisons.
Output of the code should look somewhat like this (student names have been obfuscated):
```
Student34
[1, 2, 3, 7, 6, 8, 9, 4, 5]
Student35
[9, 1, 2, 3, 6, 4, 8, 5, 7]

[0, 2, 2, 2, 2, 2, 2, 2, 1]
[0, 0, 2, 2, 2, 2, 2, 2, 1]
[0, 0, 0, 2, 2, 2, 2, 2, 1]
[0, 0, 0, 0, 2, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 2, 2, 0, 1, 2, 1]
[0, 0, 0, 1, 1, 1, 0, 1, 1]
[0, 0, 0, 1, 2, 0, 1, 0, 1]
[1, 1, 1, 2, 2, 1, 1, 1, 0]
Total amount of 1s: 22

Tudeng: Student1                  koondkaugus: 938
Tudeng: Student2                  koondkaugus: 1284
Tudeng: Student3                  koondkaugus: 1310
Tudeng: Student4                  koondkaugus: 908
Tudeng: Student5                  koondkaugus: 862
Tudeng: Student6                  koondkaugus: 1210
Tudeng: Student7                  koondkaugus: 900
Tudeng: Student8                  koondkaugus: 972
Tudeng: Student9                  koondkaugus: 1042
Tudeng: Student10                 koondkaugus: 926
Tudeng: Student11                 koondkaugus: 1258
Tudeng: Student12                 koondkaugus: 1084
Tudeng: Student13                 koondkaugus: 1150
Tudeng: Student14                 koondkaugus: 1070
Tudeng: Student15                 koondkaugus: 962
Tudeng: Student16                 koondkaugus: 1000
Tudeng: Student17                 koondkaugus: 1226
Tudeng: Student18                 koondkaugus: 1074
Tudeng: Student19                 koondkaugus: 1516
Tudeng: Student20                 koondkaugus: 964
Tudeng: Student21                 koondkaugus: 1186
Tudeng: Student22                 koondkaugus: 1010
Tudeng: Student23                 koondkaugus: 930
Tudeng: Student24                 koondkaugus: 1206
Tudeng: Student25                 koondkaugus: 1004
Tudeng: Student26                 koondkaugus: 988
Tudeng: Student27                 koondkaugus: 1000
Tudeng: Student28                 koondkaugus: 972
Tudeng: Student29                 koondkaugus: 1054
Tudeng: Student30                 koondkaugus: 1176
Tudeng: Student31                 koondkaugus: 1362
Tudeng: Student32                 koondkaugus: 926
Tudeng: Student33                 koondkaugus: 1524
Tudeng: Student34                 koondkaugus: 1062
Tudeng: Student35                 koondkaugus: 848

Student35 848
Student33 1524

Discriminating male and female rankings (most popular to most unpopular)
Most popular choices columnwise for all: [2, 1, 3, 5, 6, 4, 8, 6, 7]
Most popular choices columnwise for males: [2, 1, 3, 5, 4, 1, 6, 6, 7]
Most popular choices columnwise for females: [1, 2, 3, 4, 6, 4, 8, 5, 7]

Has first and last ranking as most popular for all males: Student22, M
Has first and last ranking as most popular for all females: Student12, N
Has first and last ranking as most popular for all females: Student14, N
Has first and last ranking as most popular for all females: Student23, N
```
where the student with the shortest and longest Kendall-Tau distance have been highlighted along with some other information required by the homework.

##### Still in progress to figure out an algorithm how to find a ranking sequence with the shortest or longest Kendall-Tau distance...
Running this code should be fairly easy since it requires no external libraries other than the base python3 installation.
How to run the script:
```
python3 tp.py
```
