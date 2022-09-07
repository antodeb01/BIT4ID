#!/bin/sh
# chkconfig: 123 69 68
# description: Hello World application init script

# Source function library.
. /etc/init.d/functions

start() {
    echo -n "Start Subscriber application"
    source /data/.env
    python3 /app/Subscriber/Subscriber.py
}

stop() {
    kill -9 `pidof helloworld`
}

case "$1" in 
    start)
       start
       ;;
    stop)
       stop
       ;;
    restart)
       stop
       start
       ;;
    status)
       # code to check status of app comes here 
       # example: status program_name
       ;;
    *)
       echo "Usage: $0 {start|stop|status|restart}"
esac

exit 0 