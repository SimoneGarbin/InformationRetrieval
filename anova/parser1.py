import numpy as np
import scipy.io

i_map = 0
i_rprec = 0
i_p10 = 0

mapi_array = np.empty([50,4])
rpreci_array = np.empty([50,4])
p10i_array = np.empty([50,4])

# file parsing
for line in open('measuresrun1ignore.txt','r'):
    
    # create map matrix
    if ' map ' in line:
        line = line.split(" ")
        mapi_array[i_map,0] = np.double(line[23])
        i_map+=1
        
    # create Rprec matrix
    if 'Rprec ' in line:
        line = line.split(" ")
        rpreci_array[i_rprec,0] = np.double(line[19])
        i_rprec+=1

    # create Precision at 10 Matrix
    if ' P_10 ' in line:
        line = line.split(" ")
        p10i_array[i_p10,0] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun2ignore.txt','r'):
    
    #create map matrix
    if ' map ' in line:
        line = line.split(" ")
        mapi_array[i_map,1] = np.double(line[23])
        i_map+=1
    
    # create Rprec matrix
    if 'Rprec ' in line:
        line = line.split(" ")
        rpreci_array[i_rprec,1] = np.double(line[19])
        i_rprec+=1
    
    # create Precision at 10 Matrix
    if ' P_10 ' in line:
        line = line.split(" ")
        p10i_array[i_p10,1] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun3ignore.txt','r'):
    
    #create map matrix
    if ' map ' in line:
        line = line.split(" ")
        mapi_array[i_map,2] = np.double(line[23])
        i_map+=1
    
    # create Rprec matrix
    if 'Rprec ' in line:
        line = line.split(" ")
        rpreci_array[i_rprec,2] = np.double(line[19])
        i_rprec+=1

    # create Precision at 10 Matrix
    if ' P_10 ' in line:
        line = line.split(" ")
        p10i_array[i_p10,2] = np.double(line[22])
        i_p10+=1


i_map = 0
i_rprec = 0
i_p10 = 0

for line in open('measuresrun4ignore.txt','r'):
    
    #create map matrix
    if ' map ' in line:
        line = line.split(" ")
        mapi_array[i_map,3] = np.double(line[23])
        i_map+=1
    
    # create Rprec matrix
    if 'Rprec ' in line:
        line = line.split(" ")
        rpreci_array[i_rprec,3] = np.double(line[19])
        i_rprec+=1
   
   # create Precision at 10 Matrix
    if ' P_10 ' in line:
        line = line.split(" ")
        p10i_array[i_p10,3] = np.double(line[22])
        i_p10+=1

#save data for matlab
scipy.io.savemat('data_ignore.mat', dict(mapi_array=mapi_array, rpreci_array=rpreci_array, p10i_array=p10i_array))
