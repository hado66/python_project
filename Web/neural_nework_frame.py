#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : neural_nework_frame.py
@Time    : 2019/2/19 10:44
@Author  : ZiyuanWang
@Software: PyCharm
"""
import numpy as np
import scipy.special
import matplotlib.pyplot as plt


class NeuralNetwork(object):
    # initialise the neural network
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes=inputnodes  #784
        self.hnodes=hiddennodes   #100
        self.onodes=outputnodes  #10

        #learing rate
        self.lr=learningrate

        # self.W_ih=(np.random.rand(self.hnodes,self.inodes)-0.5)
        # self.W_ho=(np.random.rand(self.onodes,self.hnodes)-0.5)

        # activation function is the sigmoid function
        self.activation_function=lambda x: scipy.special.expit(x)

        """有人喜欢用稍微复杂的方法来创建初始随机权重，他们使用正态分布概率分布采样权重，其中平均值，
    为0，标准方差为节点传入链接数目的开方，即1/sqrt(传入链接数目)"""
        self.W_ih=np.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))  #100*784
        self.W_ho=np.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))  #10*100
    # train the neural network
    def train(self,inputs_list,targets_list):
        inputs = np.array(inputs_list, ndmin=2).T  #784*1
        targets=np.array(targets_list,ndmin=2).T  #10*1

        hidden_inputs = np.dot(self.W_ih, inputs)  #100*1  =dot(100*784,784*1)
        hidden_outputs = self.activation_function(hidden_inputs) #100*1
        final_inputs = np.dot(self.W_ho, hidden_outputs)  #   10*1 = dot(10*100,100*1)
        final_outputs = self.activation_function(final_inputs)  #10*1

        output_errors=targets-final_outputs  # targets为 10*1，（之前转置过）
        hidden_errors=np.dot(self.W_ho.T,output_errors)  #100*1 = dot(100*10,10*1)
        self.W_ho+=self.lr*np.dot((output_errors*final_outputs*(1.0-final_outputs)),np.transpose(hidden_outputs)) #10*100 = dot(10*1,1*100)
        self.W_ih+=self.lr*np.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),np.transpose(inputs))#   100*784 = dot(100*1,1*784)

        return self.W_ih,self.W_ho
    """建议每次训练5*1000次之后，将W_ih和W_ho的数据保存在本地，numpy提供了这个保存方式
    eg:  a=np.array([[1,2,3],[7,8,9]])
         np.save("whi.npy",a)
         d=np.load("whi.npy")
    """


    # query the neural network
    def query(self,inputs_list):
        inputs=np.array(inputs_list,ndmin=2).T
        hidden_inputs=np.dot(self.W_ih,inputs)
        hidden_outputs=self.activation_function(hidden_inputs)
        final_inputs=np.dot(self.W_ho,hidden_outputs)
        final_outputs=self.activation_function(final_inputs)
        return  final_outputs

    # print  authority given image （execl data to image）
    def pri_original_image(self,image_data):
        image_data=image_data.split(',')
        image_array=np.asfarray(image_data[1:]).reshape(28,28)
        plt.imshow(image_array,cmap="Greys",interpolation='None')
        print("训练完毕！你想要测试的图片已经打印出来。。。。。")
        plt.show()


if __name__ == '__main__':
    input_nodes=784
    hidden_nodes=100
    output_nodes=10
    learningrate=0.2
    n=NeuralNetwork(input_nodes,hidden_nodes,output_nodes,learningrate)
    training_data_file=open(r"C:\Users\Administrator\Desktop\mnist_train_100.csv","r")
    training_data_list=training_data_file.readlines()
    training_data_file.close() #don't forgent close
    len_max=len(training_data_list)

    while True:
        try:
            index_image = int(input("请您输入需要判断第多少张图片："))
        except Exception:
            print("你的输入有误！")
            continue
        if index_image<0 or index_image>len_max-1:
            print("总共有 %s - %s 张图片," % (0, len_max - 1))
            continue
        else:
            break

    for record in training_data_list:
        all_values=record.split(",")
        inputs=(np.asfarray(all_values[1:])/255.0*0.99)+0.01 # 1*784
        targets=np.zeros(output_nodes)+0.01   # 1*10
        targets[int(all_values[0])]=0.99
        test=n.train(inputs,targets)
        a,b=test
        # print(a)
        # print(b)


    all_values=training_data_list[index_image]
    n.pri_original_image(all_values)

    test_set=training_data_list[index_image].split(",")
    inputs_test=(np.asfarray(test_set[1:])/255.0*0.99)+0.01
    c=n.query(inputs_test) #10*1
    print(c)
    c=c.tolist()
    print("这张图片的数值应该为： ",c.index(max(c)))

    # np.argmax(c)  #即求c最大值的索引





"""第80、33、22、43张对比错误"""

