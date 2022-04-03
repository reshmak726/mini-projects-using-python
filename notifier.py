from email import message
from socket import timeout
from turtle import title
from plyer import notification
import time 

if __name__ == '__main__':
    while True:
        notification.notify(
            title="take rest",
            message="rest is important so please have a break ....",
            timeout=5
    
        )
        time.sleep(60*60)