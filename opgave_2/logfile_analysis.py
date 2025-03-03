with open("opgave_2/app_log.txt", "r") as logFile:
    with open("opgave_2/filtered_messages.txt", "w") as filteredLogs:
        while True:
            line = logFile.readline()
            if line == "":
                break
            
            if line.find("ERROR") != -1:
                filteredLogs.write(line)
            if line.find("WARNING") != -1:
                filteredLogs.write(line)