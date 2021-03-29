f=open('ms_sec_min_hr.txt','r')
a=f.readlines()

j=[]
for i in a:
    j.append(int(i.replace("\n", "")))

def ms_sec_min_hr(j):
    ms_conversion_hr = x / 1000 / 60 / 60
    return (ms_conversion_hr)
for x in (j):
    print(ms_sec_min_hr(j))
