people=[{"arnav":19},
        {"rohan":13},
        {"pranish":25},
        {"kabindra":12}]
new_list =[i for i in people if list(i.values())[0]>18]
print(new_list)
        
        
