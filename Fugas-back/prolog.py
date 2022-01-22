from swiplserver import PrologMQI, PrologThread

def questions():
    return [
        {'id': 1, 'question': '¿Existe una fuga por desgaste natural?'},
        {'id': 2, 'question': '¿Existe una fuga por desgaste de exposición de tuberías?'},
        {'id': 3, 'question': '¿Existe una presión de agua por consumo de agua?'},
        {'id': 4, 'question': '¿Existe mantenimiento por duración del material?'},
        {'id': 5, 'question': '¿Existe afectación del lugar?'},
        {'id': 6, 'question': '¿Existen factores visibles?'},
    ]

def inicio():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query('consult("./prolog.pl")')
            result = prolog_thread.query("status(X, Y).")
            return result

def uno(answer):
    answer = answer.split(';')
    X = answer[0]
    Y = answer[1]
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query('consult("./prolog.pl")')
            result = prolog_thread.query(f"antiguedad_instalacion({X}), existe_desgaste({Y}, {X}).")
            print(result)
            return result
def dos(answer):
    answer = answer.split(';')
    X = answer[0]
    Y = answer[1]
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query('consult("./prolog.pl")')
            result = prolog_thread.query(f"antiguedad_instalacion({X}), existe_desgaste_exposicion({Y}, {X}).")
            print(result)
            return result