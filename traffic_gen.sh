echo "Enter Instance IP"
read ip
password=velocloud
funcA(){
nohup sshpass -p $password ssh root@$ip -p 2003 iperf -s --udp -i 0.5 >> iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2001 iperf -c 10.0.3.25 -u -t 120 -i 0.5  >> iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2001 iperf -c 10.0.5.25 -u -t 120 -i 0.5 >>iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2005 iperf -s --udp -i 0.5 >> iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2005 iperf -s --udp -i 0.5 >>iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2003 iperf -c 10.0.5.25 -t 120 -i 0.5 -u  >>iperf.log &
nohup sshpass -p $password ssh root@$ip -p 2001 ping 169.254.6.18 -s 1000 -i 0.01 >>ping.log & 
nohup sshpass -p $password ssh root@$ip -p 2003 ping 169.254.6.18 -s 1000 -i 0.01 >>ping.log &
nohup sshpass -p $password ssh root@$ip -p 2005 ping 169.254.6.18 -s 1000 -i 0.01 >>ping.log & 
nohup sshpass -p velocloud ssh root@$ip -p 2001 hping3 169.254.6.18 --faster >> hping.log & 
nohup sshpass -p velocloud ssh root@$ip -p 2003 hping3 169.254.6.18 --faster >> hping.log & 
nohup sshpass -p velocloud ssh root@$ip -p 2005 hping3 169.254.6.18 --faster >> hping.log & 
}
funcB(){
nohup sshpass -p velocloud ssh root@$ip -p 2001 pkill ping &
nohup sshpass -p velocloud ssh root@$ip -p 2003 pkill ping &
nohup sshpass -p velocloud ssh root@$ip -p 2005 pkill ping &
}
case $1 in
	funcA) "$@"; exit;;
	funcB) "$@"; exit;;
esac
