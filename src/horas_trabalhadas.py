from datetime import datetime, timedelta

def formatar_horario(horario):
    if len(horario) == 4:
        horario = horario[:2] + ":" + horario[2:]
    return horario

def calcular_horas_trabalhadas(inicio, fim, intervalo="00:00"):
    formato = "%H:%M"
    try:
        inicio = formatar_horario(inicio)
        fim = formatar_horario(fim)
        intervalo = formatar_horario(intervalo)
        
        inicio_dt = datetime.strptime(inicio, formato)
        fim_dt = datetime.strptime(fim, formato)
        intervalo_dt = datetime.strptime(intervalo, formato)

        if fim_dt < inicio_dt:
            fim_dt += timedelta(days=1)

        horas_trabalhadas = (fim_dt - inicio_dt).seconds / 3600 - intervalo_dt.hour - intervalo_dt.minute / 60
        return horas_trabalhadas
    except ValueError:
        raise ValueError("Formato de hora inválido. Use HH:mm.")
