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
    
import numpy as np 
array1 = np.random.randint(10,40,size=(10, ))
array2 = np.random.randint(10,40,size=(10, ))

import pandas as pd 
st.dataframe(pd.DataFrame({'kelas A':array1,
                           'kelas B':array2 
                           })
            )

