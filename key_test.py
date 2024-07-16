from pynput import keyboard

# The event listener will be running in this block
with keyboard.Events() as events:
    # Block at most ten seconds
    event = events.get(10)
    if event is None:
        print('You did not press a key within one second')
    else:
        print('Received event {}'.format(event))

        #