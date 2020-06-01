nohup mpstat -P ALL 1 | ts '%r' >> mpstat.txt &
nohup ifstat -nb | ts '%r' >> ifstat.txt &
while [ 1 ]
do
	nohup free -m | ts '%r' >> mem.txt &
	nohup debug.py --health | ts '%r' >> health.txt &
#	nohup vc_mem_mon.sh | ts '%r' >> mem_mon.txt &
	nohup debug.py --nat_dump all orig | wc -l | ts '%r' >>nat.txt &
	nohup debug.py --tunnel_count all | grep "peer"| wc -l | ts '%r' >>tunnel.txt &
#	nohup pidstat | grep -E '*d$' >> pid.txt &
	sleep 1
done

