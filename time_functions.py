import datetime
import time 
path_time_next = "Time_to_next.txt"

# # --------------------------------ROK --------------------------------------------


def data_years (liness):
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

    return sum_years


# --------------------------------ROK --------------------------------------------
# --------------------------------miesiac ----------------------------------------
def data_months(liness):
    lines_months = liness [5:7]
    sum_months = 0 

    for i in range (5,7) :
        switcher = {
            5: (int(lines_months[0]) * 10),
            6: (int(lines_months[1]) * 1)
        }
        sum_months += switcher[i]

    return (sum_months)
# --------------------------------miesiac --------------------------------------
# --------------------------------h --------------------------------------------
def data_h(liness):
    lines_h = liness[11:13]
    sum_h = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_h[0]) * 10),
            1: (int(lines_h[1]) * 1)
        }
        sum_h += switcher[i]
    return (sum_h)

# --------------------------------h ----------------------------------------------
# --------------------------------min --------------------------------------------
def data_min(liness):
    lines_min = liness[14:16]
    sum_min = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_min[0]) * 10),
            1: (int(lines_min[1]) * 1)
        }
        sum_min += switcher[i]
    return (sum_min)

# --------------------------------min --------------------------------------------
# -------------------------------sek ---------------------------------------------
def data_sek(liness):
    lines_sek = liness[17:19]
    sum_sek = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_sek[0]) * 10),
            1: (int(lines_sek[1]) * 1)
        }
        sum_sek += switcher[i]
    return (sum_sek)
# -------------------------------sek---------------------------------------------
#-------------------------------dni----------------------------------------------
def data_day(liness):
    lines_day = liness[8:10]
    sum_sek = 0 

    for i in range (0,2) :
        switcher = {
            0: (int(lines_day[0]) * 10),
            1: (int(lines_day[1]) * 1)
        }
        sum_sek += switcher[i]
    return (sum_sek)
#-------------------------------dni----------------------------------------------