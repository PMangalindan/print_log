def plog(string, log_only=False):
    """prints and logs string"""
    global session_id #so it wont have to create multiple text file for every plog call. this will ensure that only one text file will be generated for every session.
    string = str(string)
    if log_only == False: #prints if log_only is false default is false
        
        print(string)
    try:
        session_id = session_id # checks if session_id is defined 
    except:
        from datetime import datetime
        date_now = datetime.now().strftime("%m-%d-%y_%H%M%S")  # defines the session id
        session_id = str(date_now)
    output_folder = r'print_log\\'    # this is the log folder path
    try:
        if os.path.exists(output_folder): # checks if folder already exist, if not the it will create one
            pass
        else:    
            os.mkdir(output_folder)
    except:
        import os
        if os.path.exists(output_folder): 
            pass
        else:    
            os.mkdir(output_folder)
    with open(f'{output_folder}/plog_{session_id}.txt', 'a') as f: #saves the string in the text file 
        f.write(string)
        f.write('\n')
    return
plog('pol')