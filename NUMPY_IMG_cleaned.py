#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


from PIL import Image


# In[ ]:


ram_img=Image.open(r'C:\Users\akaft\OneDrive\Desktop\ramadan image.jpg')
ram_img


# In[ ]:


plt.axis("OFF")


# In[ ]:


ram_img


# In[ ]:


plt.imshow(ram_img)


# In[ ]:


plt.show()


# In[ ]:


ram_img


# In[ ]:


plt.axis("OFF")


# In[ ]:


ram_img


# In[ ]:


plt.imshow(ram_img)


# # pixel of this image
# 

# In[ ]:


ram_img.size#pixel of image in (width * height)


# In[ ]:


ram_img.format#format of image


# In[ ]:


ram_img.mode#mode of image


# In[ ]:


ram_img.resize


# In[ ]:


resized_img=ram_img.resize((50,80))
resized_img


# In[ ]:


resized_img.size


# In[ ]:


crop_img=ram_img.crop((10, 10, 500, 400))  


# In[ ]:


crop_img


# In[ ]:


crop_img.size


# In[ ]:


crop_img.show()


# In[ ]:


ram_img.copy()


# In[ ]:


ram_img.size


# In[ ]:


mount_img = Image.open(r'C:\Users\akaft\OneDrive\Desktop\mountain_image.jpg')
mount_img


# In[ ]:


type(mount_img)


# In[ ]:


type(ram_img)


# In[ ]:


mount_arr=np.asarray(mount_img)


# In[ ]:


mount_arr


# In[ ]:


type(mount_arr)


# In[ ]:


mount_arr.shape


# In[ ]:


plt.imshow(mount_img)


# In[ ]:


mount_copy =mount_img.copy()


# In[ ]:


mount_copy


# In[ ]:


mount_arr == mount_copy


# In[ ]:


mount_carr = np.asarray(mount_copy)


# In[ ]:


mount_carr


# In[ ]:


mount_arr == mount_carr


# In[ ]:


plt.imshow(mount_img)


# In[ ]:


mount_img


# In[ ]:


mount_arr1=np.array(mount_img)
mount_arr1


# In[ ]:


#jpg file not work
plt.imshow(mount_img[:,:,0], cmap="red")


# In[ ]:


mt_img=Image.open(r'C:\Users\akaft\Downloads\mountain_image.png')
mt_img


# In[ ]:


mt_arr=np.asarray(mt_img)
mt_arr


# In[ ]:


plt.imshow(mt_arr[:,:,0])


# In[ ]:


plt.imshow(mt_arr[:,:,0], cmap='gray')#use single quotes


# In[ ]:


plt.imshow(mt_arr[:,:,0], cmap='gray')#use single quotes


# In[ ]:


plt.imshow(mt_arr[:,:,0], cmap = 'Blues')


# In[ ]:


plt.imshow(mt_arr[:,:,0], cmap = 'Reds')


# In[ ]:


plt.imshow(mt_arr[:,:,0], cmap = 'plasma')


# In[ ]:


plt.imshow(mt_arr[:,:,2], cmap = 'plasma')


# In[ ]:


mt_arr[:,:,0]



# In[ ]:


mt_arr[:,:,1]


# In[ ]:


mt_arr[:,:,2]


# In[ ]:


mt_arr[:,:,2] = 0


# In[ ]:


#it work in copy img
mt_arr= np.array(mt_img).copy()


# In[ ]:


mt_arr


# In[ ]:


mt_arr[:,:,2] = 0


# In[ ]:


mt_arr[:,:,2]


# In[ ]:


plt.imshow(mt_arr)


# In[ ]:


mt_arr


# In[ ]:


mount_arr


# In[ ]:


arr1=np.asarray(mt_img)


# In[ ]:


arr1


# In[ ]:


type(arr1)


# In[ ]:


arr1.shape


# In[ ]:


plt.imshow(arr1)


# In[ ]:


mt_img1 = arr1.copy()


# In[ ]:


mt_img1[:,:,0] = 0


# In[ ]:


plt.imshow(mt_img1)


# In[ ]:


mt_img1[:,:,1]


# In[ ]:


mt_img1[:,:,1] = 1


# In[ ]:


plt.imshow(mt_img1)


# In[ ]:




