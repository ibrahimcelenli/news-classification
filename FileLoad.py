# -*- coding: utf-8 -*-

import os   #operating system
import random
import pandas



class fileLoad(object):
    
    
    

        

    #data is load 
    def load2(self):
        
        
        rootdir = "haber1150"  #folder name
        
        #Information about files
        
        #for directories, subdirs, files in os.walk(rootdir): 
            #print(directories, subdirs, len(files)) 
        
        
        ekonomi_list = []
        magazin_list = []
        saglik_list = []
        siyasi_list = []
        spor_list = []
        combined_list = []


        #files are read end labeled
        for directories, subdirs, files in os.walk(rootdir):
            if (os.path.split(directories)[1]  == 'ekonomi'):
                for filename in files:      
                    with open(os.path.join(directories, filename), encoding="Windows-1254") as f:
                        data = f.read()

                
                        ekonomi_list.append((data, "ekonomi")) #added to list

    
            if (os.path.split(directories)[1]  == 'magazin'):
                for filename in files:
                    with open(os.path.join(directories, filename), encoding="Windows-1254") as f:
                        data = f.read()

                
                        magazin_list.append((data, "magazin"))
                
                
        for directories, subdirs, files in os.walk(rootdir):
            if (os.path.split(directories)[1]  == 'saglik'):
                for filename in files:      
                    with open(os.path.join(directories, filename), encoding="Windows-1254") as f:
                        data = f.read()

                        saglik_list.append((data, "saglik"))
    
            if (os.path.split(directories)[1]  == 'siyasi'):
                for filename in files:
                    with open(os.path.join(directories, filename), encoding="Windows-1254") as f:
                        data = f.read()

        
                        siyasi_list.append((data, "siyasi"))
                
                
        for directories, subdirs, files in os.walk(rootdir):
            if (os.path.split(directories)[1]  == 'spor'):
                for filename in files:      
                    with open(os.path.join(directories, filename), encoding="Windows-1254") as f:
                        data = f.read()

      
                        spor_list.append((data, "spor"))
           
            
        #If you want to see the data    
        """        
        print(ekonomi_list[0])
        print("----------------------------------------------------------------------------------------------")
        print(magazin_list[0])
        print("----------------------------------------------------------------------------------------------")
        print(saglik_list[0])
        print("----------------------------------------------------------------------------------------------")
        print(siyasi_list[0])
        print("----------------------------------------------------------------------------------------------")
        print(spor_list[0])
        """
        
        """
        print(len(ekonomi_list))
        print(len(magazin_list))
        print(len(saglik_list))
        print(len(siyasi_list))
        print(len(spor_list))
        print(len(ekonomi_list+magazin_list+saglik_list+siyasi_list+spor_list))
        """

        combined_list = ekonomi_list + magazin_list + saglik_list + siyasi_list + spor_list
        print("\n")
        print("\n")
        print("Sum Data Number :  ",len(combined_list))

        random.shuffle(combined_list) #mix the data

        # creating dataFrame and the combined_list is transferred
        daf = pandas.DataFrame(combined_list, columns=['message', 'label'])

        # print (daf) #space to separete.

        daf['length'] = daf['message'].map(lambda text: len(text))

        print("\n")
        print("Summary")
        print("\n")
        print(daf.groupby('label').describe())            # summary

        # print (daf.head(10))                            #character legth
        # daf.length.plot(bins=10, kind='hist')           #histogram
        # daf.hist(column='length', by='label', bins=5)   #According to label histogram
        print("\n")
        print("\n")
        print("First 10 Data")
        print(daf.message.head(10))
        
        return daf






