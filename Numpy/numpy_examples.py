import numpy as np

print('************  array  *****************************')
a = np.array([1, 2, 3, 4, 5])
print(a)
<<<<<<< HEAD
print('mean:' + str(np.mean(a)))

b = np.array([[2,3,4],[12,13,14]])
print('b.size={0:3d}'.format(b.size))
print('np.size(b,0)={0:3d}'.format(np.size(b,0)))
print('np.size(b,1)={0:3d}'.format(np.size(b,1)))

print(b.shape)
print('b.shape[0]={0:3d}'.format(b.shape[0]))
print('b.shape[1]={0:3d}'.format(b.shape[1]))
print('b.shape[1]={0:3d}'.format(b.shape[1]))
print('b.shape[1]={0:3d}'.format(b.shape[1]))
print('b.shape[1]={0:3d}'.format(b.shape[1]))
print('b.shape[1]={0:3d}'.format(b.shape[1]))
=======
print('mean: ' + str(np.mean(a)))
print('a.ndim :' + str(a.ndim))
print('a.size: ' + str(a.size))
print('a.dtype: ' + str(a.dtype))
print('a.dtype.name: ' + str(a.dtype.name))
print('a.data: ' + str(a.data))
ad = np.array([1, 2, 3.0, 4, 5])
print(ad)
print('mean: ' + str(np.mean(ad)))
print('ad.ndim :' + str(ad.ndim))
print('ad.size: ' + str(ad.size))
print('ad.dtype: ' + str(ad.dtype))
print('ad.data: ' + str(ad.data))
print('************  arange  *****************************')
b = np.arange(15).reshape(3, 5)
print(b)
print('mean: ' + str(np.mean(b)))
print('b.ndim :' + str(b.ndim))
print('b.size: ' + str(b.size))
print('b.shape: ' + str(b.shape))
print('b.shape[0]: ' + str(b.shape[0]))
print('b.shape[1]: ' + str(b.shape[1]))
print('b.dtype: ' + str(b.dtype))
print('b.dtype.name: ' + str(b.dtype.name))
print('b.data: ' + str(b.data))
bd = np.arange(15.0).reshape(3, 5)
print(bd)
print('mean: ' + str(np.mean(bd)))
print('bd.ndim :' + str(bd.ndim))
print('bd.size: ' + str(bd.size))
print('bd.shape: ' + str(bd.shape))
print('bd.shape[0]: ' + str(bd.shape[0]))
print('bd.shape[1]: ' + str(bd.shape[1]))
print('bd.dtype: ' + str(bd.dtype))
print('bd.dtype.name: ' + str(bd.dtype.name))
print('bd.data: ' + str(bd.data))
>>>>>>> 624d99f41b399dc46fee4651960ee603903c1919
