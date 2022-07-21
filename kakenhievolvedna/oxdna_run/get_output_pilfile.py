#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil
import glob
import subprocess as sp
import config as cfg

all_results_dir = "../results"


# In[2]:


#条件ごとのpeppercorn実行結果のディレクトリ一覧を"パス名で"得る
def get_result_dir_path(all_results_dir):
    peppercorn_results = glob.glob("{}/peppercorn*".format(all_results_dir))
    #print_lit(peppercorn_results)
    return peppercorn_results
    #output : list of "resluts/(peppercorn output libraries)"
    
all_results_correction= get_result_dir_path(all_results_dir)#結果ファイルのフォルダ名


# In[3]:


#display(all_results_correction)


# In[4]:


#ディレクトリ一覧を受け取り、連番による簡略な名前にする
def simplify_dirname(dirlist, parent_dirname):
    counter = 0
    for dirname in dirlist:
        counter = counter + 1
        print("old_filename : ", dirname)
        print("new filename : ", parent_dirname + "/peppercorn_result"+str(counter))
        shutil.move(dirname, parent_dirname +"/peppercorn_result"+str(counter))
    dirlist = get_result_dir_path(parent_dirname)
    print("directory name was modified : \n", dirlist)
    return dirlist

simplify_dirname(all_results_correction, "../results")


# In[5]:


def cut_parent_dir(filepath, parent_dir):
    newfilepath = filepath.replace(parent_dir+"/", "")
    return newfilepath
#cut_parent_dir("../results/output.pil", "../results")


# In[ ]:


for results_dir_path in all_results_correction:
    
    results_dir_name = cut_parent_dir(results_dir_path, all_results_dir)
    #results/<ある条件でのpeppercorn実行結果ディレクトリ> の１つ
    print("ライブラリパス：", results_dir_path, "\n")
    print("ライブラリ名：", results_dir_name, "\n")
    
    print("-----------------------------sim : {} start--------------------------------".format(results_dir_name))
    
    result_files = glob.glob("{}/output*.pil".format(results_dir_path))
    #print("result_files : ", result_files, "\n")
    #result_filesは、
    #results内の複数ライブラリそれぞれにあるoutput***.pilのパスを抽出した一覧
    
    #各実行条件dirにあるpilファイル全てについて：
    
    counter_filename = 0
    
    for result_file in result_files:
        counter_filename = counter_filename + 1
        print("結果ファイル：", result_file, "\n")

        output_folder = ("./sim_result_"+results_dir_name+"_"+str(counter_filename))
        #output_folder = "sim_result" + str(counter_dirname)
        print( "oxdna実行結果出力先：", output_folder, "\n")
        
    
        exeprogram = "python3"
        exefile = "./main.py"
        executable = [exeprogram, exefile, result_file, output_folder]
        print("executable : ", executable)
        #python3 argv[0]:main.py argv[1]:<result pilfile> argv[2]:<output folder>
        logfile = "log"+results_dir_name+".txt"
        with open(logfile,"w") as log:
            runned = sp.run(executable, stdout=log, stderr=sp.STDOUT, text=True)
            shutil.copy(result_file, output_folder)

        print("実行コマンド：")
        #display(executable)
        
    print("-----------------------------sim : {} end--------------------------------".format(results_dir_name))

    


# In[ ]:





# In[ ]:





# In[ ]:




