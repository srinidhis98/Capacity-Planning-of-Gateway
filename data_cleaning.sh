

cat health.txt | grep 'flow' >>flow.txt
sed 's/,//g' flow.txt >>flow1.txt
cat health.txt | grep 'handoff' >>handoff.txt
cat mpstat.txt| awk '{print $1, $2"|", $5"|", $6,"|" $8,"|", $15}' >> mp_modif.txt
cat mem.txt | grep 'Mem' >>mem_modif.txt

