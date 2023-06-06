#!/usr/bin/env python
# coding: utf-8

# In[22]:


def plog(string):
    """prints and logs string"""
    global session_id
    string = str(string)
    
    
    print(string)
    
    
    
    try:
        
        session_id = session_id
        
    except:
        from datetime import datetime
        date_now = datetime.now().strftime("%m-%d-%y_%H%M%S") 
        session_id = str(date_now)
        
        
    output_folder = r'print_log\\'    
    
    try:
        
        if os.path.exists(output_folder): 
            pass
        else:    

            os.mkdir(output_folder)
    except:
        import os
        if os.path.exists(output_folder): 
            pass
        else:    

            os.mkdir(output_folder)
        
    with open(f'{output_folder}/plog_{session_id}.txt', 'a') as f:
        f.write(string)
        f.write('\n')
    
    return string

