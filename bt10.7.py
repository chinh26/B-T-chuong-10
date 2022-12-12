# in chuỗi s 
str = 'a b c d e f duck'
# loại bỏ khoảng trắng ở đầu và cuối chuỗi
print (str.strip())
# in chuỗi vs kí tự đầu chuỗi viết hoa
print ( str.capitalize())
# đếm và in số lần chuỗi con s_sub xuất hiện trong chuỗi s
s_sub = 'd';
print (str.count(s_sub, 7, 18))
# tìm kiếm s_find và thay thế bằng s_replace sau đó in chuỗi sau khi tìm kiếm và thay thế 
s_find = 'cat';
print ( str.find ( s_find, 9, 18 ))