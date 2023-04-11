FROM vulfocus/webmin-cve_2021_31760

RUN apt-get install -y sudo
RUN apt-get remove -y wget

# Create a new normal user without sudo permission
RUN useradd -m myuser && \
    echo 'myuser:password' | chpasswd

# Write the flag to the file
RUN echo "Here is the second part of the flag: [_CVE_3xpl01t]" > /home/myuser/2nd_part_of_the_flag.txt
RUN echo "Here is the third part of the flag: [_@and_pr1v!l3g3_3scal@tion_1s_s0_fUn!}]" > /root/3rd_part_of_the_flag.txt

RUN echo "myuser ALL=(root) NOPASSWD: /usr/sbin/service webmin start" >> /etc/sudoers

# Disable root login
RUN passwd -d root

# Change root password
RUN /usr/share/webmin/changepass.pl /etc/webmin root ac28ad543f41d087f89d261feba59dc8

# Disable SSL
# RUN sed -i 's/ssl=1/ssl=0/g' /etc/webmin/miniserv.conf

# Change ownership of Webmin directories to myuser
RUN chown -R myuser: /usr/share/webmin /etc/webmin /var/webmin
RUN chmod 777 /tmp

# Add write permission to /etc/shadow for all users
RUN chmod 666 /etc/shadow

# Set the default user to myuser and start Webmin
USER myuser
ENTRYPOINT [ "/docker-entrypoint.sh" ]
#CMD ["sudo", "/usr/sbin/service", "webmin", "start"]