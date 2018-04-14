from gpiozero import Button
import subprocess
from signal import pause

def shutdown():
    print("Halting system...")
    subprocess.check_call(['sudo', 'poweroff'])

def kill_pico8():
    print("Killing PICO-8...")
    try:
        subprocess.check_call(['killall', 'pico8'])
    except subprocess.CalledProcessError, e:
        print "PICO-8's already dead baby, PICO-8's already dead.\n"#, e.output

lightning_button = Button(17, hold_time=5)
lightning_button.when_held = shutdown
lightning_button.when_pressed  = kill_pico8

pause()
