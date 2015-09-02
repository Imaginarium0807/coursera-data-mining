#!/usr/bin/python

    
def split_file(cat_filename):
    
    cat_file = open(cat_filename, 'r')
    #Write file into list
    reviews_list = []
    business_name = ''
    
    for line in cat_file:
        #Skip blank lines
        if line in ['\n', '\r\n']:
            pass
             
        if 'Business_Name:' in line:
            prev_business_name = business_name
            business_name = ''.join(line.strip().split()[1:])
            business_name = business_name.replace('/','_')

            if len(reviews_list)>0:
                write_business_file(reviews_list, prev_business_name, cat_filename)
                del reviews_list[:] 
        
        else:
            reviews_list.append(line)

    cat_file.close()

def write_business_file(reviews_list, business_name, cat_filename):

    business_file = open(business_name+'_'+cat_filename, 'w')

    for review in reviews_list: 
        business_file.write(review)
    
    business_file.close()


def main():
    
    cat_filename = 'Barbeque.txt'
    split_file(cat_filename)

if __name__=="__main__":
    main()

