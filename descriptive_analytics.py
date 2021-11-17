#!/usr/bin/env python
# coding: utf-8

# # Identitas

# In[ ]:


# Nama      : Salma Sari Juliani
# NIM       : 19921122
# Deskripsi : Praktikum Pengenalan Komputasi Modul 3


# # Code

# # Soal 1

# In[ ]:


import pandas as pd
data_frame = pd.read_csv("C:/Programming Things/Data/covid19.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows' , None)


# In[ ]:


# 1. Data ke-10
data_frame.loc[9]


# In[ ]:


# 2. Data ke-115 hingga ke 125
data_frame[114:125]


# In[ ]:


# 3. Data kolom New Cases hingga Total Recovered dengan indeks 20
print(data_frame.loc[20, "New Cases":"Total Recovered"])


# In[ ]:


# 4. Data ketika kasus baru lebih dari 2000 atau kematian baru lebih dari 50
data_frame.loc[(data_frame["New Cases"] > 2000) & (data_frame["New Deaths"] > 50)]


# In[ ]:


# 5. Data ketika kasus baru bernilai maksimum dan data ketika kasus baru 
#    bernilai minimum

print('New Cases Maksimum :', data_frame.max()['New Cases'])
print('New Cases Minimum :', data_frame.min()['New Cases'])


# In[ ]:


# 6. Jangkauan Total Kasus
maksimum = data_frame.max()
minimum = data_frame.min()
range = maksimum['Total Cases'] - minimum['Total Cases']
print('Range :', range)


# In[ ]:


# 7. Data yang diurutkan berdasarkan Case Fatality Rate secara menurun
data_frame.sort_values(['Case Fatality Rate'], ascending=[0])


# In[ ]:


# 8. Statistik sederhana data
data_frame.describe()


# In[ ]:


# 9. Pandang kolom New Cases hingga Total Recovered. Dengan kolom manakah kolom
#    New Active Cases paling berkorelasi? Tampilkan koefisien korelasinya.

print(data_frame['New Active Cases'].corr(data_frame['New Cases']))
print(data_frame['New Active Cases'].corr(data_frame['New Deaths']))
print(data_frame['New Active Cases'].corr(data_frame['New Recovered']))
print(data_frame['New Active Cases'].corr(data_frame['Total Cases']))
print(data_frame['New Active Cases'].corr(data_frame['Total Deaths']))
print(data_frame['New Active Cases'].corr(data_frame['Total Recovered']))


# Kolom New Active Cases paling berkorelasi dengan kolom New Cases.
# Korelasi antara kedua kolom tersebut semakin Berbanding Lurus dengan nilai 
# koefisien korelasinya : 0.7065623475058376


# In[ ]:


# 10. Dataframe menjadi csv baru
data_frame.to_csv("covid_new.csv")


# # Soal 2

# In[ ]:


univ = pd.read_csv("C:/Programming Things/Data/universities.csv")
score = pd.read_csv("C:/Programming Things/Data/score_science.csv")
majors = pd.read_csv("C:/Programming Things/Data/majors.csv")


# In[ ]:


# universities.csv


# In[ ]:


# 1. Data ke-75 dan seterusnya
univ[74:]


# In[ ]:


# 2. Data ke-70 hingga ke-80
univ[69:80]


# In[ ]:


# 3. Data ITB
univ.loc[(univ['university_name'] == 'INSTITUT TEKNOLOGI BANDUNG')]


# In[ ]:


# majors.csv


# In[ ]:


# 4. Data dengan capacity maksimum serta dengan capacity minimum

print('Capacity Maksimum :', majors.max()['capacity'])
print('Capacity Minimum :', majors.min()['capacity'])


# In[ ]:


# 5. Range dari capacity
maksimum = majors.max()
minimum = majors.min()
range = maksimum['capacity'] - minimum['capacity']
print('Range :', range)


# In[ ]:


# 6. Data yang universitasnya merupakan ITB, kemudian urutkan berdasarkan
#    capacity secara menaik

majors1 = majors.loc[majors['id_university'] == 332]
majors1.sort_values(['capacity'], ascending=[1])


# In[ ]:


# 7. Frekuensi munculnya nilai kolom id_university

majors['id_university'].value_counts()


# In[ ]:


# score_science.csv


# In[ ]:


# 8. Kelompokkan data berdasarkan kolom id_first_university, kemudian 
#    tampilkan rata-rata kolom score_kua-nya

score.groupby("id_first_university")["score_kua"].mean()


# In[ ]:


# 9. Tampilkan hanya kolom skor-skor saja
score1 = score.loc[ : ,"score_bio":"score_ppu"]
score1


# In[ ]:


# 10. Tampilkan statistik sederhana dari tabel yang diperoleh dari nomor 9
score1.describe()


# In[ ]:




