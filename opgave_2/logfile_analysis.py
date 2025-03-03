with open("opgave_2/app_log.txt", "r") as logFile:
    with open("opgave_2/warnings.txt", "w") as warnings:
        with open("opgave_2/errors.txt", "w") as errors:
            while True:
                line = logFile.readline()
                if line == "":
                    break
                if line.find("ERROR") != -1:
                    errors.write(line)
                if line.find("WARNING") != -1:
                    warnings.write(line)