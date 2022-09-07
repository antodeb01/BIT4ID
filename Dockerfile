FROM  devhub-docker.cisco.com/iox-docker/ir800/base-rootfs as builder
RUN opkg update && opkg install python 
RUN opkg install iox-toolchain
RUN mkdir -p /app/Subscriber
COPY requirements.txt /app/Subscriber 
COPY DB.py /app/Subscriber
COPY Subscriber.py /app/Subscriber
WORKDIR /app/Subscriber
COPY init_app.sh /etc/init.d/
RUN chmod +x /etc/init.d/init_app.sh
RUN update-rc.d init_app.sh defaults


