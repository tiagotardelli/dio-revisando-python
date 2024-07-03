## O que é o módulo datetime?
O módulo 'datetime' em Python é usado para lidar com datas e horas. Ele possui
várias classes úteis como date, time e timedelta
```python
import datetime

d = datetime.date(2032, 7, 19)
print(d)
#>>>2023-07-19
```

## Manipulando Datas
Podemos criar e manipular objetos date, time e datetime de várias maneiras.
Por exemplo, podemos adicionar e subtrair datas, verificar a difrença entre
datas e muito mais.
```python
import datetime

d = datetime.daterime(2023, 7, 19, 13, 45)
print(d)
#>>>2023-07-19 13:45:00
d = d + datetime.timedelta(weeks=1)
print(d)
#>>>2023-07-26 13:45:00
```

## Formatando e Convertendo datas com strftime e strptime
Python também permite converter e formatar datas e horas. Para isso, usamos
os métodos 'strftime' (string format time) e 'strptime' (string parse time)
```python
from datetime import datetime

d = datetime.now()

print(d.strftime("%d/%m/%Y %H:%M")) # 03/07/2023 05:05

date_string = "20/07/2023 15:30"
d = datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(d) # 2023-07-20 15:30:00
```

## Time zone
Quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python
facilita isso através do módulo 'pytz'
```python
from datetime import datetime

import pytz

d = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d) # 2024-07-03 05:10:00-03:00
```