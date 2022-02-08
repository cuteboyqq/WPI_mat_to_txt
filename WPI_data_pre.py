# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:14:09 2022

@author: User
"""
import os
from scipy import io
from PIL import Image
import glob  # 文件搜索匹配
import numpy as np
from to_JPEGImages import home


trainval_seqs = ['seq1', 'seq2', 'seq3', 'seq4', 'seq5', 'seq6', 'seq7']
test_seqs = ['seq1', 'seq2', 'seq3', 'seq4', 'seq5', 'seq6', 'seq7', 'seq8', 'seq9', 'seq10',
             'seq11', 'seq12', 'seq13', 'seq14', 'seq15', 'seq16', 'seq17']
splits = {'test': test_seqs,
          'trainval': trainval_seqs

# 以下两个参数需根据文件路径修改
newpath = r"C:\Users\zh99\Desktop\database\VOC2007\JPEGImages"  # VOC数据集JPEGImages文件夹路径
home = r"C:\Users\zh99\Desktop\database\WPI"  # wpi数据集路径




def Analysis_path(mat_path):
    mat_dir = os.path.dirname(mat_path)
    file = mat_path.split(os.sep)[-1]
    return mat_dir, file

def read_mat(mat_dir):
    
    mat_path_list = glob.iglob(os.path.join(mat_dir,"*.mat"))
    gt_dic = {}
    for mat_path in mat_path_list:
        print(mat_path)
        
        mat_dir, mat_file = Analysis_path(mat_path)
        mat_dict = io.loadmat(mat_path)  # 加载mat文件 返回字典
        gt_data = mat_dict['GroundTruth']
        gt_data = gt_data.squeeze()
        #mat_dict = np.array(mat_dict)
        #print(gt_data)
        '''
        for i in gt_data:
            print('aaaaaaaaaaaaaaaaa')
            #print(i)
            i_data = i.squeeze()
            #i_data = i_data.squeeze()
            #i_data = i_data.squeeze()
            print(i_data)
        '''
        #gt_data = np.array(gt_data)
        
        object_num = len(gt_data)
        print(object_num)
        frame_num = 0
        for i in range(object_num):  # 得到图片数量
            temp_num = gt_data[i][-1][-3]
            print("temp_num",i)
            #print(temp_num)
            if temp_num > frame_num:
                frame_num = temp_num
        print(frame_num)
        gt = [[] for i in range(frame_num)]
        #print(gt)
        
        
        for obejct in gt_data:
            for frame in obejct:
                #print(frame)
                #frame = list(frame)
                #print(frame)
                gt[frame[-3] - 1].append(frame)
        gt_dic[mat_file] = gt
        
    return gt_dic

def create_txt(gt_dic, split, imagepath):
    """
    将字典的数据写入txt文件
    :param gt_dic: 从mat读取的数据
    :param split:
    :param imagepath: 图片存放路径
    :return:
    """
    file_path = os.path.join(home, 'annotation.txt')
    gtdata_txt = open(file_path, 'a')  # 若文件已存在,则将数据写在后面而不是覆盖 --'a'
    for seq, data in gt_dic.items():
        for frame_id, objects in enumerate(data):
            gtdata_txt.write('%s_%s_%s' % (split, seq[:-4], str(data[frame_id][0][-3]).rjust(4, '0')))
            for x, y, w, h, _, _, label in objects:
                coordinate = change_coordinate(x, y, w, h)
                label = label - 1
                gtdata_txt.write(" " + ",".join([str(a) for a in coordinate]) + ',' + str(label))
            gtdata_txt.write('\n')
    gtdata_txt.close()

def creat_annotation():
    for split in txt_splits:
        gt_dic = read_mat(home, split)
        create_txt(gt_dic, split, ImagePath)
        
        
if __name__=="__main__":
    mat_dir = r"D:\Frames_GT_Lights\labels\matlab"
    
    #read_mat(mat_dir)
    
    creat_annotation()
    