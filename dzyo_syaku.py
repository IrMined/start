import numpy
# 1 тё  = 3600 сун
# 1 дзё = 100 сун
# 1 сяку = 10 сун
# Входной параметр целочисленно делим на 3600. Результат деления это значение тё
# Остаток от деления, полученный в предыдущем пункте целочисленно делим на 100. Результат деления это значение дзё
# Остаток от деления, полученный в предыддущем пункте целочисленно делим на 10. Резултат деления это значение сяку.
# Остаток от деления, полученный в предыдущем пункте это значение сун.
def getTransfer(N):
    tyo = N//3600
    dzyo = (N - tyo * 3600) // 100
    syaku = (N - tyo *3600 - dzyo*100)//10
    sun = N - tyo *3600 - dzyo*100 - syaku*10
    print(str(tyo) + " " + str(dzyo) + " " + str(syaku) + " " + str(sun))

getTransfer(5000)