from threading import Event
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

exit = Event()


def main():
    print('chime.py - Play an alert every X seconds')
    try:
        interval = int(input('How many seconds between chimes? '))
        print('Press Ctrl+C to exit.')
    except ValueError as e:
        print(f'Could not interpret input: {e}')
        exit.set()

    pygame.mixer.init()
    pygame.mixer.music.load('Maj5_ascending.mp3')

    while not exit.is_set():
        pygame.mixer.music.play()
        exit.wait(interval)
    print('\nExiting.')


def quit(_signo, _frame):
    exit.set()


if __name__ == '__main__':
    import signal

    for sig in ('TERM', 'HUP', 'INT'):
        signal.signal(getattr(signal, 'SIG' + sig), quit)

    main()
