def obj_read(file_path):
    for x in range(10):
        print("")
    f = open(file_path, "r")
    #print(f.read()) 
    null = "null"
    #flags
    v_flag = False
    pass_flag = False
    space_flag1 = False
    #ver int
    x = ""
    y = ""
    z = ""
    clock = 0
    spacer = 0


    for row in f:
        if (row[0]) == "v" and (row[1]) == " ":
            #print(row)
            lang = len(row)
            xyz = -1
            for char in range(lang):
                if xyz == 0:
                    if (row[char]) == " ":
                        xyz = 1
                    else:
                        x =  x +(row[char])
                if xyz == 1:
                    if (row[char]) == " ":
                        xyz = 2
                    else:
                        y = y + (row[char])
                if xyz == 2:
                    if (row[char]) == " ":
                        pass
                    else:
                        z = z + (row[char])
            print(x + "X")
            print (y + "Y")
            print(z + "Z")
                
                
           
        
        
    print(x)
    #print (y)
    #print(z)
            


        
                        




    #data seperater

    x_full =null
    y_full =null
    z_full =null