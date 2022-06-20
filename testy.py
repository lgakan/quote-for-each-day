import datetime
import time 
path = "C:/Users/pol4_/Desktop/New folder (2)/Tutaj.xtt"


now_3 = datetime.datetime.now()
print(now_3.strftime("%y-%m-%d %H:%M:%S"))


with open(path, 'w') as f:
    data = now_3
    f.write(str(data))
#----------------------------------------------

time.sleep(2)
with open(path, 'r') as f:
    random = f.read()

now_2 = datetime.datetime.now()


result = map(lambda x: x, random)
result_2 = map(lambda x: x, str(now_2))


print(random)
# --------------------------------ROK --------------------------------------------
liness = list(result)

def data_years ():
    lines_years = liness[0:4]
    sum_years= 0 
    for i in range (0, 4):
        switcher = {
            0: (int(lines_years[0]) * 1000),
            1: (int(lines_years[1]) * 100),
            2: (int(lines_years[2]) * 10),
            3: (int(lines_years[3]) * 1)
        }
        sum_years += switcher[i]

    print(sum_years)
    return sum_years


# --------------------------------ROK --------------------------------------------

# --------------------------------miesiac --------------------------------------------
def data_months():
    lines_months = liness [5:7]
    sum_months = 0 

    for i in range (5,7) :
        switcher = {
            5: (int(lines_months[0]) * 10),
            6: (int(lines_months[1]) * 1)
        }
        sum_months += switcher[i]

    print(sum_months)
# --------------------------------miesiac --------------------------------------------


# DNI NIE POTRZEBUJA PETLI 

# --------------------------------h --------------------------------------------
def data_days():
    lines_h = liness[11:13]
    sum_h = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_h[0]) * 10),
            1: (int(lines_h[1]) * 1)
        }
        sum_h += switcher[i]
    print(sum_h)

# --------------------------------h -------------------------------------------------

# --------------------------------min --------------------------------------------
def data_min():
    lines_min = liness[14:16]
    sum_min = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_min[0]) * 10),
            1: (int(lines_min[1]) * 1)
        }
        sum_min += switcher[i]
    print(sum_min)

# --------------------------------min --------------------------------------------
