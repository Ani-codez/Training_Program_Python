d={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
def translate(st):
    for i in st.split():
        if i in d.keys():
            print(d[i],end=" ")
        else:
            print(i,end="")

s=input()
translate(s)
