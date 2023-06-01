def operaciones(pnumeroa,pnumerob,pResSuma,pResResta):
    return pnumeroa,pnumerob,pResSuma+1,pResResta-1


mia=4
mib=5
miS=0
miR=0
mia,mib,miS,miR=operaciones(mia,mib,miS,miR)
print(f"No cambian {mia},{mib} y emule referencia con {miS} y {miR}")