def accum(string):
    st = []
    List = list(string)
    for i in range(len(List)):
        st.append( List[i].upper() + (((i) * List[i]).lower()) )
        
        
    x = str("-".join(st))
    return x
