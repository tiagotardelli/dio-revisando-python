from datetime import timedelta, datetime

def tempo_lavagem(tipo_carro):
    tempo_pequeno = 30
    tempo_medio = 45
    tempo_grande = 60
    
    data_atual = datetime.now()
    
    match tipo_carro:
        case "P":
            data_estimada = data_atual + timedelta(minutes=tempo_pequeno) 
            print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
        case "M":
            data_estimada = data_atual + timedelta(minutes=tempo_pequeno) 
            print(f"O carro chegou: {data_atual} e ficará pronto às {tempo_medio}")
        case "G":
            data_estimada = data_atual + timedelta(minutes=tempo_pequeno) 
            print(f"O carro chegou: {data_atual} e ficará pronto às {tempo_grande}")

def tempo_cronometro(tempo):
    data_estimada = datetime.now() + timedelta(seconds=tempo)
    print(data_estimada)
    while True:
    
        print(datetime.now())
        if data_estimada >= datetime.now():
            print("finalizado")
            break
        else:
            print(datetime.now() - timedelta(seconds=1))
        
if __name__ == "__main__":
    tempo_lavagem('P')
    tempo_cronometro(5)
    print(datetime.now().date())