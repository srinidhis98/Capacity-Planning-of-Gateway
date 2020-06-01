
# For filterinng flows from the health.txt
cat health.txt | grep 'flow' | awk '{print $1, $2"|", $4}'  >>flow.txt
sed 's/,//g' flow.txt >>flow1.txt
mv flow1.txt flow.txt
# For filtering handoffq-drops from health.txt
cat health.txt | grep 'handoff'|  awk '{print $1, $2"|", $4}' >>handoff.txt
# for filtering required params such as CPU, %usr, %sys, %idle from mpstat.txt
sed -e '/Average/d' mpstat.txt >>mp.txt
sed -e '1,2d' mp.txt >>mp_new.txt
cat mp_new.txt| awk '{print $1, $2"|", $5"|", $6,"|" $8,"|", $15}'>> mp_modif.txt
sed 's/ CPU//g' mp_modif.txt  >>mp1.txt
sed 's/%idle//g' mp1.txt >>mp2.txt
sed 's/%sys//g' mp2.txt >>mp3.txt
sed 's/%usr//g' mp3.txt >>mp_final.txt
mv mp_final.txt mp_modif.txt
rm mp.txt
rm mp_new.txt
rm mp1.txt
rm mp2.txt
rm mp3.txt
rm mp_modif.txt
# for filtering Mem from mem.txt
cat mem.txt | grep 'Mem' >>mem_modif.txt
awk '{print $1, $2"|", $4"|", $5"|", $6"|", $7"|", $8"|", $9}' mem_modif.txt >> mem_final.txt
mv mem_final.txt mem_modif.txt
# making file suitable to converted to .csv
cat nat.txt | awk '{print $1, $2"|", $3}' >>nat_modif.txt
# making file suitable to converted to .csv
cat tunnel.txt | awk '{print $1, $2"|", $3}' >>tun_modif.txt
# making file suitable to converted to .csv
sed -e '1,2d' ifstat.txt >>if_new.txt
cat if_new.txt | awk '{print $1, $2"|", $3"|", $4"|", $5"|", $6"|", $7"|", $8"|", $9"|", $10"|", $11"|", $12}' >>ifstat_modif.txt

