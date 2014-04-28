#!/bin/bash
awk -F " " '{print $1" "$4}' log | awk -F "[" '{print $1" "$2}' | awk -F ":" '{print $1":"$2":"$3}' > newlog

echo "The unique ip address is: "
cat newlog | sort -t " " -k1,1 -u
echo -e "\n" "The number of unique ip address is: "
cat newlog | sort -t " " -k1,1 -u | wc -l
echo -e "\n" "The visit time of ip address in one minute is: "
cat newlog | awk '{print $1$2}' | awk '{a[$1]++}END{for(i in a){print i " " a[i]}}'
echo -e "\n" "The abnormal ip address is: "
cat newlog | awk '{print $1$2}' | awk '{a[$1]++}END{for(i in a){print i " " a[i]}}' | grep -n ' [3-9][0-9]\{1\}'