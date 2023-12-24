# 使用方法：

from Acb import Acb

# 实例化一个Acb对象
acb = Acb()

# 调用方法
print(acb.get_acbs())
print(acb.get_acbs(1))
print(acb.get_acbs(1, 2))
print(acb.get_acbs(1, 2, 3))
print(acb.get_acbs(1, 2, 3, 4))
print(acb.get_acbs(1, 2, 3, 4, 5))


print(acb.get_acb_by_id(1))
print(acb.get_acb_by_id(2))
print(acb.get_acb_by_id(3))
print(acb.get_acb_by_id(4))

print(acb.get_acb_by_name('中文'))
print(acb.get_acb_by_name('英文'))
print(acb.get_acb_by_name('日文'))
print(acb.get_acb_by_name('韩文'))
print(acb.get_acb_by_name('西班牙文'))
