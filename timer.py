from plyer import notification
import time

secondsInput = int(input('Enter the no of seconds : \n'))

while True:
    if secondsInput >= 1:
        secondsInput = secondsInput - 1
        sleep = time.sleep(secondsInput)
        break
    else:
        break


notification.notify(
            title='Timer by Venkat',
            message='The timer of has been timed out',
            app_icon='D:\Sai\Programming Projects\Python Projects\Timer\clock.ico',
            timeout=5
        )

print('The timer of has been timed out ')



