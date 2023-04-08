# library
import streamlit as st

# write
st.title ('software perkalian')
st.write ('ini adalah aplikasi yang dibuat menggunakan streamlit')

# input bilangan pertama 
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

# input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

# hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else :
    st.write ('Silahkan pencet tombol hitung!!')
    
import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'Kelas A': array1,
                            'Kelas B': array2}))