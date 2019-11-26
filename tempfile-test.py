#!/usr/bin/env python
# coding: utf-8

# In[77]:


import os 


# In[58]:


import tempfile


# In[107]:


###  1. TemporaryFile() 建立一個臨時file，當關閉時被刪除

###  tempfile. TemporaryFile(mode=’w+b’, buffering=None, encoding=None, newline=None, suffix=none, prefix=None, dir=None)
     # mode=’w+b’ 表示二進位制模式，確保了它的行為在所有平臺上始終保持一致，若要改本文模式則是mode=’w+t’
     # buffering = 0/1/>1，0代表buffer關閉（適用於二進位模式），1代表line buffer（適用於文本模式），>1表示初始化的buffer大小
     # encoding 表示的是返回的數據採用何種編碼，一般採用utf8或gbk
     # newline = None,\n,\r,'','\r\n'，用于區分換行符號，但這個參數只對本文模式有效
     # suffix,prefix,dir 可用來控制文件名和路徑

# 建立並開啟暫存檔案（二進位）
fp = tempfile.TemporaryFile()

# 寫入二進位資料
fp.write(b'Hello world!')


# In[108]:


# 將文件指到最開始處準備讀取文件
fp.seek(0)

# 讀取檔案內容
fp.read()


# In[109]:


os.path.exists(fp.name)


# In[110]:


# 關閉檔案（自動刪除檔案）
fp.close()


# In[111]:


os.path.exists(fp.name)


# In[91]:


###  2. NamedTemporaryFile() 建立一個【有文件名】的臨時file，可用於要將文件名传傳遞给其他代碼来打開这个文件的时候使用，當關閉時被刪除

###  tempfile. NamedTemporaryFile(mode=’w+b’, buffering=None, encoding=None, newline=None, suffix=None, dir=None, delete=True)
     #若不想在close後自動刪除則將 delete=false即可

    
# 建立並開啟暫存檔案（二進位）    
fp1 = tempfile.NamedTemporaryFile()

#確認檔案名稱和路徑
fp1.name


# In[99]:


#確認檔案是否存在
os.path.exists(fp1.name)


# In[93]:


fp1.write(b'Hello world!')


# In[97]:


# read data from file
fp1.seek(0)
fp1.read()


# In[90]:


fp1.close()


# In[84]:


os.path.exists(fp1.name)


# In[85]:


### 3. use "with"

with tempfile.NamedTemporaryFile() as fp2:
    fp2.write(b'Hello world!')
    print(fp2.name)
    fp2.seek(0)
    print(fp2.read())
    print(os.path.exists(fp2.name))


# In[86]:


print(os.path.exists(fp2.name))
#use"with", the file will close automaticlly.


# In[112]:


### 4. tempfile.TemporaryDirectory() 建立一個臨時目錄，可在暫存目錄中可以存放任意數量的暫存檔

### tempfile. TemporaryDirectory(suffix=None, prefix=None, dir=None)
from tempfile import TemporaryDirectory
with TemporaryDirectory() as fp:
    print('臨時目錄名:', fp)


# In[ ]:


### 5. tempfile.mkstemp() 建立臨時文件，但要自己刪除，較低級別，且不能與with一起使用
### 6. tempfile.mkdtemp() 建立臨時目錄，但要自己刪除，較低級別，且不能與with一起使用
### 7. tempfile.SpooledTemporaryFile 建立臨時目錄，和 TemporaryFile 函數相比，當程序像該臨時文件輸出數據時，會先輸出到內存中，直到超過 max_size 才會真正输出到物理磁盤中
### 8. gettempdir() 獲取系统的臨時目錄
### 9. gettempprefix() 返回臨時文件的prefix名稱。

