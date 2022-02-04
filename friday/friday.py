"""
ID: jessety1
LANG: PYTHON3
TASK: friday
"""

day_Of_Week = -1
#0 = monday, 1 = tuesday, 2 = wednesday and so on 3 th 4 fri 5sat 6sun
day_Of_Month = 0
month_of_year = 1
year = 1900
final = [0] * 7

with open('friday.in','r') as fin:
    num_Of_Years = int(fin.readline().strip())



for i in range (num_Of_Years):
    if year%400 == 0 or (year%4 == 0 and year%100 !=0):
       for i in range (366):
            day_Of_Month += 1
            day_Of_Week += 1
            if month_of_year == 1 or month_of_year == 3 or month_of_year == 5 or month_of_year == 7 or month_of_year == 8 or month_of_year == 10 or month_of_year == 12:
                if day_Of_Month > 31:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year == 4 or month_of_year == 6 or month_of_year == 9 or month_of_year == 11:
                if day_Of_Month > 30:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year == 2:
                if day_Of_Month > 29:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year > 12:
                month_of_year = 1
            if day_Of_Week > 6:
                day_Of_Week = 0
            if day_Of_Month == 13:
                final[day_Of_Week] += 1
    else: 
         for i in range (365):
            day_Of_Month += 1
            day_Of_Week += 1
            if month_of_year == 1 or month_of_year == 3 or month_of_year == 5 or month_of_year == 7 or month_of_year == 8 or month_of_year == 10 or month_of_year == 12:
                if day_Of_Month > 31:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year == 4 or month_of_year == 6 or month_of_year == 9 or month_of_year == 11:
                if day_Of_Month > 30:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year == 2:
                if day_Of_Month > 28:
                    day_Of_Month = 1
                    month_of_year +=1
            if month_of_year > 12:
                month_of_year = 1
            if day_Of_Week > 6:
                day_Of_Week = 0
            if day_Of_Month == 13:
                #print (f"day of week:{day_Of_Week}")
                final[day_Of_Week] += 1
            
    year += 1

#print(final[5:]+final[:5])
result = final[5:]+final[:5]
result2 = [f"{i}" for i in result]
with open ('friday.out','w') as fout:
          
    fout.write(' '.join(result2)+"\n")

