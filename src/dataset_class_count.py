import shutil
import os, sys
import multiprocessing
import yaml

class DatasetClassification():
    def __init__(self):
        ### load param
        try:
            config_name = './param/' + 'dataset_class_count.yaml'
            with open(config_name) as file:
                self.yaml = yaml.load(file, Loader=yaml.FullLoader)
        except:
            exit('ERROR: dataset_class_count.yaml not defined.') 
            
        self.dataset_path = self.yaml['dataset_path']
        dataset_file_list = os.listdir(self.dataset_path)
        self.txt_list = [file for file in dataset_file_list if file.endswith(".txt")]
        self.label_dict = self.yaml['some_dict']

    def classifier(self,i=None):        
        # count=0
        # start = i
        # end = i+4999
        # jpg_list_split = self.jpg_list[start:end]
        len_txt=len(self.txt_list)
        count=0
        for filename in self.txt_list:
            # im1 = Image.open(self.load_img_path+filename)
            # print(filename)
            
            fr = open(self.dataset_path+'/'+filename, mode='r')
            lines = fr.readlines()
            for i in range(0, len(lines)):
                label_data = lines[i].split(" ")
                label_data = label_data[0]
            
                for key, value in self.label_dict.items():
                    if label_data == key:
                        self.label_dict[key] += 1
            count+=1
            print(str(count)+'/'+str(len_txt))
        for key in self.label_dict:
            print(str(key)+":"+str(self.label_dict[key]))
            
            
            
    
def main():
    dc = DatasetClassification()
    dc.classifier()

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: ')
        exit('$ python dataset_class_count.py')
    main()
    
    