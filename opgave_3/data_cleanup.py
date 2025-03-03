import re

with open("opgave_3/source_data.csv", "r") as source:
    with open("opgave_3/cleaned_data.csv", "w") as destination:
        with open("opgave_3/discard_log.csv", "w") as discard:
            while True:
                line = source.readline()
                if line == "":
                    break
                data = line.split(",")
                if len(data) > 4:
                    for entry in data:
                        if entry == "":
                            data.remove(entry)
                try: 
                    if int(data[0]) < 0:
                        discard.write("Id must be positive in: " + line)
                        continue
                except ValueError or IndexError:
                    discard.write("Id not int in: " + line)
                    continue
                try: 
                    data[1] = data[1].strip()
                    assert re.match(r'([a-zA-Z]+?.([\s][a-zA-Z]?.)+)+', data[1])
                except AssertionError or IndexError:
                    discard.write("Name not valid in: " + line)
                    continue
                try:
                    assert re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                                    data[2])
                except AssertionError or IndexError:
                    discard.write("Email not valid in: " + line)
                    continue
                try:
                    float(data[3])
                except ValueError or IndexError:
                    discard.write("Amount not a float in: " + line)
                    continue
                destination.write(",".join(data))

                



                    



            
            
            



