#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
import re
import glob
import subprocess as sp
import config as cfg


# In[18]:


import sys
display(sys.version)
display(sys.path)


# In[19]:


#条件ごとのpeppercorn実行結果のディレクトリ一覧を"パス名で"得る
def get_result_dir_path(all_results_dir):
    peppercorn_results = glob.glob("{}/peppercorn*".format(all_results_dir))
    #print_lit(peppercorn_results)
    return peppercorn_results
    #output : list of "resluts/(peppercorn output libraries)"
"""
all_results_dir = "../results"
all_results_correction = get_result_dir_path(all_results_dir)
all_results_correction"""


# In[20]:


#１つの結果ディレクトリ or pilファイルのパス名と、
#それが属している親ディレクトリのパスを受け取り、
#親ディレクトリパスを除いた結果ディレクトリの名前を返す。
def erase_parent_dir_path(peppercorn_result_dir, results_dir):
    result_dir_name =  peppercorn_result_dir.replace(results_dir+"/", "").partition('.pil')[0]
    return result_dir_name
"""
results_dir = "../results"
erase_parent_dir_path(all_results_correction[0], results_dir)"""


# In[21]:


all_results_dir = "../results"
all_results_correction= get_result_dir_path(all_results_dir)

for results_dir_single in all_results_correction:
    #results_dir_single : 
    #results/<ある条件でのpeppercorn実行結果ディレクトリ> の１つ
    result_dir_name = erase_parent_dir_path(results_dir_single, all_results_dir)
    print("ライブラリパス：", results_dir_single, "\n")
    print("ライブラリ名：", result_dir_name, "\n")
    result_files = glob.glob("{}/output*.pil".format(results_dir_single))
    #result_filesは、
    #results内の複数ライブラリそれぞれにあるoutput***.pilを抽出した一覧

    for result_file in result_files:
        #print("結果ファイル：", result_file, "\n")
        
        output_folder = "sim_result_" + erase_parent_dir_path(result_file, all_results_dir)
        
        print( "oxdna実行結果出力先：\n", output_folder)
        exeprogram = "python3"
        exefile = "./main.py"
        executable = [exeprogram, exefile, result_file, output_folder]
        #python3 argv[0]:main.py argv[1]:<result pilfile> argv[2]:<output folder>
        sp.run(executable, stdout=sp.DEVNULL, stderr = sp.DEVNULL)
        logfile = "log"+result_dir_name+".txt"
        with open(logfile,"w") as log:
            runned = sp.run(executable, stdout=log, stderr=sp.STDOUT, text=True)
        print(runned)


# In[ ]:





# In[ ]:




