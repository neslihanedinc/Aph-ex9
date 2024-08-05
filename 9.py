def reversed_string(text):
    reversed_string=''
    #boş string başlattım
    for char in text:
        reversed_string= char + reversed_string
#ilk karakter n ,sonra n'in önüne e ekliyorum derken döngü son harfe kadar devam
    return reversed_string
data="neslihan"
print(reversed_string(data))

#palindromu da böyle yap




