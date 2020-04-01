import math
import tree

class C45:

    def __init__(self, data_path):
        self.data_path = data_path

        #assumes the last column is the Class
        self.classes=[] #list of all classes
        self.num_class = 0

        self.attributes = [] #list of all attributes
        self.num_attribute= 0   

        self.data=[]
        

    def data_fill(self):
        data_file=open(self.data_path, "r")

        #Fill class names
        temp = data_file.readline()
        self.classes =temp.split(",")
        self.classes[-1]=self.classes[-1].strip()
        self.num_class=len(self.classes)

        #Fill attribute names
        temp = data_file.readline()
        self.attributes=temp.split(",")
        self.attributes[-1]=self.attributes[-1].strip()
        self.num_attribute=len(self.attributes)

        #fill data
        temp = data_file.readline()
        while (temp):
            data_row_s=temp.strip()
            data_row_l=data_row_s.split(",")
            if(len(data_row_l)==self.num_attribute+1):
                for i in range(self.num_attribute):
                    #print(data_row_l[i])
                    data_row_l[i]=float(data_row_l[i])
            self.data.append(data_row_l)
            temp = data_file.readline()
        data_file.close()




    #returns tuple of number of remaining classes and list of said classes
    def num_classes_in_data(self, data):
        class_lst=[]
        for i in data:
            if i[-1] not in class_lst:
                class_lst.append(i[-1])
                if (len(class_lst) == self.num_class):
                    return self.num_class,class_lst
        if (len(class_lst)==0):
            return 0,["no class"]
        return len(class_lst),class_lst

    #calculates the entropy of a dataset.
    #week 5 ID3-C45 page 12-13
    def calc_entropy(self,data):
        num_rows=len(data)
        if (num_rows < 1):
            return 0
        class_cnt_lst=[0]*self.num_class
        for i in data:
            if (i[-1] in self.classes):
                class_cnt_lst[self.classes.index(i[-1])] += 1
        for i in range(len(class_cnt_lst)):
            class_cnt_lst[i]=float(class_cnt_lst[i]/num_rows)
        #print(class_cnt_lst)
        entropy=0
        for i in class_cnt_lst:
            if (i!=0):
                entropy -= i * math.log(i,2)
        return entropy-1
    
    #calculates the gain of a binary split on a dataset
    #week 5 ID3-C45 page 13-15
    def calc_gain(self, data, subset1, subset2):
        base_entropy=self.calc_entropy(data)
        s1_entropy=self.calc_entropy(subset1)
        s2_entropy=self.calc_entropy(subset2)
        gain=base_entropy-(s1_entropy+s2_entropy)
        return gain


    #details in documentation
    def determine_best_split(self,data):
        best_attrib=0
        subset1=[]
        subset2 =[]
        best_gain=0
        best_split_val=0
        for attrib in range(self.num_attribute):
            sorted_data=sorted(data,key=lambda l:l[attrib], reverse=True)
            for i in range(len(data)-1):
                if(sorted_data[i][-1] != sorted_data[i+1][-1]):
                    split_val=sorted_data[i][attrib]
                    more=sorted_data[:i+1]
                    less=sorted_data[i+1:]
                    test_gain=self.calc_gain(data,more,less)
                    if (test_gain > best_gain):
                        best_attrib=attrib
                        subset1=more
                        subset2=less
                        best_gain=test_gain
                        best_split_val=split_val
        return best_attrib,subset1,subset2,best_split_val

    #recurisivly builds a decision tree from the dataset
    def build_decision_tree(self):
        info =self.num_classes_in_data(self.data)
        d_tree=tree.Node(str(info[1][0]), 1.0)
        #print(info[0])
        if (info[0] > 1):
            d_tree=self.build_decision_tree_r(self.data,tree.Node("",1))
        else:
            d_tree=tree.Node(str(info[1][0]), 1.0)
        d_tree.print_tree(d_tree)

    def build_decision_tree_r(self,data,d_tree):
        t_node=d_tree
        info =self.num_classes_in_data(data)
        #print(info)
        if (info[0] > 1):
            split_info=self.determine_best_split(data)
            t_node.info="Split by " +self.attributes[split_info[0]]+ " on interval "+str(split_info[3])
            t_node.childrenID=[round(t_node.id+0.1,1),round(t_node.id*10,1)]
            t_node.left=self.build_decision_tree_r(split_info[2],tree.Node("",t_node.childrenID[0]))
            t_node.right=self.build_decision_tree_r(split_info[1],tree.Node("",t_node.childrenID[1]))
        else:
            t_node.info=str(info[1][0])

        return t_node
