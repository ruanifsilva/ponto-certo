import calendar
from datetime import date, datetime, timedelta

data = "20/12/2021"
data_convertida = datetime.strptime(data, "%d/%m/%Y")
hora = timedelta(days=2)
data_convertida += hora

print(data_convertida)
print((data_convertida - datetime.now()).days)

print(calendar.month(2021, 12))
print(calendar.monthrange(2021, 12))
print(calendar.weekday(2021, 12, 8))
print(list(calendar.day_name))


# TAREFA - colocar as views set e serializers
# estudar autenticação com JWT


# date para str
#
# hora1 = timedelta(hours=12)
# hora = datetime.now()
#
#
# print(hora.isoformat())
# print(hora.strftime('%x'))
#
#
#
