# a = 10, a adalah variabel yang menyimpan nilai 10
a= 10
# tipe data: angka satuan(integer)
data_integer = 432
print("data_integer:", data_integer)
print("bertipe:", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 3.14
print("data_float:", data_float)
print("bertipe:", type(data_float))

#tipe data: kumpulan karakter (string)
data_string = "Hello, World!"
print("data_string:", data_string)
print("bertipe:", type(data_string))

#tipe data: nilai benar/salah (boolean)
data_boolean = False
print("data_boolean:", data_boolean)
print("bertipe:", type(data_boolean))  

#tipe data khusus: None (tidak ada nilai)
data_none = None
print("data_none:", data_none)
print("bertipe:", type(data_none))

#tipe data: angka kompleks (complex)
data_complex = complex(2, 3)  # 2 adalah bagian real, 3 adalah bagian imajiner
print("data_complex:", data_complex)
print("bertipe:", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_int, c_float, c_double, c_char_p
data_c_int = c_int(42)
data_c_float = c_float(3.14)
data_c_double = c_double(2.718281828459045)
data_c_char_p = c_char_p(b"Hello, C!")
print("data_c_int:", data_c_int.value)
print("data_c_float:", data_c_float.value)
print("data_c_double:", data_c_double.value)
print("data_c_char_p:", data_c_char_p.value.decode('utf-8'))


#tipe data intger
print("\n=======Tipe Data Integer======================")
data_int = 32;
print("data_int:", data_int)

data_float = float(data_int)  # mengkonversi integer ke float
data_str = str(data_int)  # mengkonversi integer ke string
data_bool = bool(data_int)  # mengkonversi integer ke boolean  
print("data_float:", data_float)
print("data_str:", data_str)
print("data_bool:", data_bool)


#tipe data float
print("\n=======Tipe Data Float======================")
data_float = 43.4;
print("data float:",data_float, ",type:", type(data_float))

data_int = int(data_float)  # mengkonversi float ke integer
data_str = str(data_float)  
data_bool = bool(data_float)  
print("data_int:", data_int, ",type =", type(data_int))
print("data_str:", data_str,",type =", type(data_str))
print("data_bool:", data_bool, ",type =", type(data_bool))


#tipe data boolean
print("\n=======Tipe Data BOOLEAN======================")
data_bool = False;
print("data float:",data_bool, ",type:", type(data_bool))

data_int = int(data_bool)  # mengkonversi float ke integer
data_str = str(data_bool)  
data_float = float(data_bool)  
print("data_int:", data_int, ",type =", type(data_int))
print("data_str:", data_str,",type =", type(data_str))
print("data_float:", data_float, ",type =", type(data_float))

#tipe data string
print("\n=======Tipe Data STRING======================")
data_str = "10";
print("data_str:", data_str, ",type:", type(data_str))      

data_int = int(data_str)  #string harus angka
data_float = float(data_str)  #string harus angka
data_bool = bool(data_str)  #false jika string kosong
print("data_int:", data_int, ",type =", type(data_int))
print("data_str:", data_float,",type =", type(data_float))
print("data_bool:", data_bool, ",type =", type(data_bool))

