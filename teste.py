import pyautogui
import random
import time

def press_key(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def click_mouse():
    current_x, current_y = pyautogui.position()
    pyautogui.click(current_x, current_y)
    print(f'Clicando na posição atual ({current_x}, {current_y})')

def perform_random_action():
    action_prob = random.random()

    if action_prob < 0.30:  # 30% de chance de pressionar W, A, S ou D por 2 a 5 segundos
        key = random.choice(['w', 'a', 's', 'd'])
        duration = random.uniform(2, 5)  # Sorteia um tempo entre 2 e 5 segundos
        press_key(key, duration)
        print(f'Pressionando {key.upper()} por {duration:.2f} segundos')
    elif action_prob < 0.60:  # 30% de chance de pressionar W, A, S, D por 2 segundos cada tecla
        for key in ['w', 'a', 's', 'd']:
            press_key(key, 2)
            print(f'Pressionando {key.upper()} por 2 segundos')
    elif action_prob < 0.90:  # 30% de chance de apertar barra de espaço 2x
        press_key('space', 0.1)
        time.sleep(0.1)
        press_key('space', 0.1)
        print('Pressionando Barra de Espaço 2x')
        if random.random() < 0.10:
            key = random.choice(['w', 'a', 's', 'd'])
            press_key(key, 3)
            print(f'Pressionando {key.upper()} por 3 segundos')

        press_key('space', 0.1)
        time.sleep(0.1)
        press_key('space', 0.1)
        print('Pressionando Barra de Espaço 2x novamente')
    else:  
        click_mouse()

def main():
    start_time = time.time()
    last_time_check = start_time
    duration = 3 * 3600  # 3 horas em segundos

    while time.time() - start_time < duration:
        perform_random_action()
        time.sleep(random.uniform(0.5, 2))

        current_time = time.time()
        if current_time - last_time_check >= 120:  # 2 minutos = 120 segundos
            elapsed_time = current_time - start_time
            minutes, seconds = divmod(elapsed_time, 60)
            print(f'Tempo de execução: {int(minutes)} minutos e {int(seconds)} segundos')
            last_time_check = current_time

    # Impressão final do tempo de execução
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f'Tempo de execução final: {int(minutes)} minutos e {int(seconds)} segundos')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")
