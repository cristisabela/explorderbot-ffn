#/bin/bash
DATE=`date '+%Y-%m-%d %H:%M:%S'`

tshark -i eth0 -F pcap -w "/home/ec2-user/${DATE}.pcap" -f "src port 53"
