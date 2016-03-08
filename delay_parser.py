f = open("base5.txt");
f = f.readlines();

for j in range(0,len(f)/2):
	i = j*2;
	
	if(f[i].count(":")>2):
		temp1 = f[i];
		temp1 = temp1.split(":",2);
		
		temp1 = (float(temp1[0])*3600) + (float(temp1[1])*60) + (float(temp1[2].split("\t",1)[0]));

		temp2 = f[i+1];
		temp2 = temp2.split(":",2);
		
		temp2 = (float(temp2[0])*3600) + (float(temp2[1])*60) + (float(temp2[2].split("\t",1)[0]));
		
		print int((temp2 - temp1)*1000);
	else:
		temp1 = f[i];
		temp1 = temp1.split(":",1);
		
		temp1 = (float(temp1[0])*60) + (float(temp1[1].split("\t",1)[0]));

		temp2 = f[i+1];
		temp2 = temp2.split(":",1);
		
		temp2 = (float(temp2[0])*60) + (float(temp2[1].split("\t",1)[0]));
		
		print int((temp2 - temp1)*1000);
