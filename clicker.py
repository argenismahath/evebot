from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Posición del cursor: X={x}, Y={y}")

try:
    with Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
