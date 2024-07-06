def readDataFromTxt(fileName):
    data = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            splitedTemplate = line.strip().split(',')
            template = []
            for element in splitedTemplate:
                if (element != ''):
                    template.append(int(element))
            data.append(template)
    return data
            
