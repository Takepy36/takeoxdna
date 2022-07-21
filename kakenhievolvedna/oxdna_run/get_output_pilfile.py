#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
import re
import glob
import datetime
import subprocess as sp
import config as cfg


# In[2]:


#条件ごとのpeppercorn実行結果のディレクトリ一覧を"パス名で"得る
def get_result_dir_path(all_results_dir):
    peppercorn_results = glob.glob("{}/peppercorn*".format(all_results_dir))
    return peppercorn_results
    #output : list of "resluts/(peppercorn output libraries)"


# In[3]:


def cut_parent_dir(filepath, parent_dir):
    newfilepath = filepath.replace(parent_dir+"/", "")
    return newfilepath
#cut_parent_dir("../results/output.pil", "../results")


# In[4]:


def sim_all_results_dir(all_results_dir = "../results"):
    
    results_path_list= get_result_dir_path(all_results_dir)
    print("results_path_list :" , results_path_list)

    for results_dir_path in results_path_list:
    
        results_dir_name = cut_parent_dir(results_dir_path, all_results_dir)
        #results/<ある条件でのpeppercorn実行結果ディレクトリ> の１つ
        print("ライブラリパス：", results_dir_path, "\n")
        print("ライブラリ名：", results_dir_name, "\n")
        print("-----------------------------sim : {} start--------------------------------".format(results_dir_name))
        run_main_for_eachfiles(results_dir_path)
        print("-----------------------------sim : {} end--------------------------------".format(results_dir_name))


# In[5]:


def run_main_for_eachfiles(results_dir_path):
    #result_filesはresults内の複数ライブラリそれぞれにあるoutput***.pilのパスを抽出した一覧
    d = {' ' :  '_', '.' :  '', ':' : '_'}
    tbl = str.maketrans(d)
    result_files = glob.glob("{}/output*.pil".format(results_dir_path))
    for result_file in result_files:
            print("結果ファイル：", result_file, "\n")
            datetime_sim = str(datetime.datetime.now()).translate(tbl)
            
            output_folder = ("./sim_result_peppercorn_"+datetime_sim)# ??
            print( "oxdna実行結果出力先：", output_folder, "\n")


            exeprogram = "python3"
            exefile = "./main.py"
            executable = [exeprogram, exefile, result_file, output_folder]
            print("executable : ", executable)
            #python3 argv[0]:main.py argv[1]:<result pilfile> argv[2]:<output folder>
            logfile = datetime_sim+"_log.txt"
            print("log : ",logfile)
            with open(logfile,"w") as log:
                runned = sp.run(executable, stdout=log, stderr=sp.STDOUT, text=True)
                print(result_file)
                shutil.copy(result_file, output_folder)

            print("実行コマンド：")
            display(executable)
            new_logpath = shutil.move(logfile, output_folder+"/"+logfile)
            print(new_logpath)


# In[6]:


def main():
    sim_all_results_dir()


# In[ ]:


if __name__ == "__main__":
    main()

