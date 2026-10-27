def obj_read(file_path):
    f = open(file_path, "r")
    #print(f.read()) 
    null = "null"
    #flags
    v_flag = False
    pass_flag = False
    space_flag1 = False
    #ver int
    x = ""
    y = 0
    z = 0


    for row in f:
        for cell in row:
            if cell == "v":
                pass_flag = True
                v_flag = True
            if pass_flag:
                pass_flag = False
                print("pass")
                pass
            else:
                print("continue")
                if space_flag1 and not cell == " ":
                    x = (str(x) + str(cell))
                    print(x)
                elif space_flag1:
                    pass

                if v_flag and cell == " ":
                    space_flag1 = True
            


        
                        




    #data seperater

    x_full =null
    y_full =null
    z_full =null