import numpy as np
import scipy.io

i_map = 0
i_rprec = 0
i_p10 = 0

map_array = np.empty([50,4])
rprec_array = np.empty([50,4])
p10_array = np.empty([50,4])

for line in open('measuresrun1.txt','r'):
    
    if ' map ' in line:
        line = line.split(" ")
        map_array[i_map,0] = np.double(line[23])
        i_map+=1
        

    if 'Rprec ' in line:
        line = line.split(" ")
        rprec_array[i_rprec,0] = np.double(line[19])
        i_rprec+=1

    if ' P_10 ' in line:
        line = line.split(" ")
        p10_array[i_p10,0] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun2.txt','r'):
    
    if ' map ' in line:
        line = line.split(" ")
        map_array[i_map,1] = np.double(line[23])
        i_map+=1
    
    
    if 'Rprec ' in line:
        line = line.split(" ")
        rprec_array[i_rprec,1] = np.double(line[19])
        i_rprec+=1
    
    if ' P_10 ' in line:
        line = line.split(" ")
        p10_array[i_p10,1] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun3.txt','r'):
    
    if ' map ' in line:
        line = line.split(" ")
        map_array[i_map,2] = np.double(line[23])
        i_map+=1
    
    
    if 'Rprec ' in line:
        line = line.split(" ")
        rprec_array[i_rprec,2] = np.double(line[19])
        i_rprec+=1
    
    if ' P_10 ' in line:
        line = line.split(" ")
        p10_array[i_p10,2] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun4.txt','r'):
    
    if ' map ' in line:
        line = line.split(" ")
        map_array[i_map,3] = np.double(line[23])
        i_map+=1
    
    
    if 'Rprec ' in line:
        line = line.split(" ")
        rprec_array[i_rprec,3] = np.double(line[19])
        i_rprec+=1
    
    if ' P_10 ' in line:
        line = line.split(" ")
        p10_array[i_p10,3] = np.double(line[22])
        i_p10+=1


scipy.io.savemat('data.mat', dict(map_array=map_array, rprec_array=rprec_array, p10_array=p10_array))
