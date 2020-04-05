#/bin/bash
DATE=`date '+%Y-%m-%d %H:%M:%S'`

tshark -i eth0 -F pcap -w "/tmp/${DATE}.pcap" -f "src port 53"
