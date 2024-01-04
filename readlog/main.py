#bibliotecas importadas
from pymavlink import mavuitl 
from datetime import datatime

# entrada do arquivo
filename = ""

#status do arquivo 
print("processing log %s" % filename)
mlog = mavuitl.mavlink_connection(filename)
data = dict()

# condições e loop 
while True:
    m = mlog.recv_match(type="")
    if m is None:
        break
    type = m.get_type()

    data[m.TimeUS] = {
        "Volt": m.Volt,
        "Curr": m.Curr,
    }

#Print dos resultados procurados
    print(type(data))