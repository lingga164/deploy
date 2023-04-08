#library
import streamlit as st

# write
st.title("SOFTWARE PERKALIAN")
st.write("ini adalah aplikasi yang dibuat dengan streamlit")

# input bilangan pertama 
number1 = st.number_input('Masukkan bilangan pertama')
st.write('Bilangan pertama adalah:', number1)

# input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write('Bilangan kedua adalah:', number2)

#hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil Kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol Hitung!')
   
