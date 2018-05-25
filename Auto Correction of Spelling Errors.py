import tkinter                                           # For Building Graphical User Interface
from tkinter import *
from nltk.tokenize import sent_tokenize,word_tokenize
import re
#from docx import Document

import string
from tkinter import messagebox                           # For showing MessageBox
from collections import Counter
import money                                             # Package for Currency Formatting
from tkinter import font
import enchant , difflib
from enchant.tokenize import get_tokenizer
from enchant import DictWithPWL
from tkinter.font import Font
#from fuzzywuzzy import fuzz
from datetime import datetime




def left(event):
 MainWindow.title('Print Pressed')


def Clear():
    '''
    #f.write(Txt_input.get("1.0",END))
    Txt_dic.insert(INSERT,(Txt_input.get("1.0",END)))
    Word_selec.insert(INSERT,(Txt_input.get("1.0",END)))
    Txt_input.tag_add("start", "1.0", END)
    Txt_input.tag_config("start", background="yellow", foreground="green")
    Tokens = word_tokenize(Txt_input.get("1.0",END))
    print(Tokens)
    '''
    
    #Word_selec.delete(1.0,END)
    Txt_input.delete(1.0,END)
    Txt_Totl_cnt.delete(1.0,END)
    Txt_non_dupl.delete(1.0,END)
    Txt_Mispled_Word.delete(1.0,END)
    
    wrd_lstbox.delete(0,END)
    sugst_lstbx.delete(0,END)
    minm_lstbox.delete(0,END)
    #f.close()

def onclick(event):
    '''
    Tokens = word_tokenize(Txt_input.get("1.0",END))
    #print("It is pressed")
    Txt_input.tag_add("bad", "1.0",  END)
    #Txt_input.tag_config("bad", background="red", foreground="green")
    '''
    wrd_replace =""
    wrd_replace =minm_lstbox.get(ANCHOR)
    print("word replaced",wrd_replace)
    
def load_file():
   print("Start time",str(datetime.now()))
   read_line =""
   cnt_totl_wrd=0 
   non_duplcte_cnt =0
   duplcte_cnt =0
   #alredy_add   =[]
   wrd_token =""
   crps_strng =""
   
   fir =  open('D:\Word Dicitionary4.txt','r')
   fd = open('D:\Dicitionary.txt','w')

   
   for line in fir.readlines():
       fil_arr.append(word_tokenize(line))


   crps_strng = ''.join(str(wrd) for wrd in fil_arr) # Generates a String from the arraylist
   crps_strng = crps_strng.replace(']',"")
   crps_strng = crps_strng.replace('[',"")
   crps_strng = crps_strng.replace("'","")
   crps_strng = crps_strng.replace(",","")
   crps_strng = crps_strng.replace(".","")
   crps_strng = crps_strng.replace('"',"")
   crps_strng = crps_strng.replace("--","")
   crps_strng = crps_strng.replace("(","")
   crps_strng = crps_strng.replace(")","") 
   crps_strng = crps_strng.replace(":","")
   crps_strng = crps_strng.replace("!","")

   
       
   for i in  crps_strng.split():
        
       if i not in dicit_arr :
          fd.write(str(i) + "\n")
          non_duplcte_cnt+=1
          
       else:
          duplcte_cnt +=1

           
   '''
   for wd in read_line.split():
           
           if wd not in dicit_arr :
              fd.write(str(wd) + " " + "\n")  
              #print("Words in line",wd)
              dicit_arr.append(wd)
              non_duplcte_cnt+=1

           else:
  '''             
       


    
   cnt_totl_wrd =    non_duplcte_cnt+   duplcte_cnt   #Total count = Duplicate words + non Duplicate words
    

   
   #print(" \n Read Corpus",read_corps)

   '''
   for w in read_corps.split(): # To find total no of words in the Corpus including duplicates
      cnt_wrd = cnt_wrd +1
      if w not in dicit_arr :
          fd.write(str(w) + " " + "\n")
          dicit_arr.append(word_tokenize(w))
   '''
    
      
   #non_dplicte_wrd = ''.join(str(wrd) for wrd in non_duplicte) # Generates a String from the arraylist
  
  

   #for wr in  non_dplicte_wrd.split(): # To find total no of words in the Corpus excluding duplicates
      #non_duplcte_cnt +=1
      #set_crps.add(wr)


   Txt_Totl_cnt.insert(INSERT,"{:,}".format(cnt_totl_wrd))  #Insert the Total Word Count of the Corpus in the Text Box
   Txt_Totl_cnt.tag_add("start", "1.0", END)
   Txt_Totl_cnt.tag_config("start", font=("Georgia", "12", "bold"),background="yellow")
  
  #---------------------------------------------------------------------------------------------------------------------------------

   Txt_non_dupl.insert(INSERT,"{:,}".format(non_duplcte_cnt))  #Insert the Total  Count of the Words in the Corpus Excluding Duplicates in the Text Box
   Txt_non_dupl.tag_add("start", "1.0", END)
   Txt_non_dupl.tag_config("start",font=("Georgia", "12", "bold"), background="yellow")
   #print("file loaded")
   messagebox.showinfo("Title", "File Loaded Successfully" )
   fd.close()
   fir.close()
   print("End time",str(datetime.now()))

  #print("\n The number of elements in an array ",len(fil_arr))
  
  
  #print("\n The  Corpus is ",read_corps ,"\n the count of words including duplicates are ", cnt_wrd)
  #print("\n The Count of words excluding Duplicates",non_duplcte_cnt)
    
   

def find_sug_words(evt):
    suget_wrd =""
    levn_cost =0
    dict,max = {},0
    tmp =0
    wrd_lst_pair =""
    len_mispld_wrd =0
    len_corpus_wrd =0
    target = ""
    source =""
    columns=0
    rows   =0
    m=0

    #Word_selec.delete(1.0,END)
    value =wrd_lstbox.get(ANCHOR)
    
    #value = wrd_lstbox.get(wrd_lstbox .curselection())
    print("value",value)
    
    #Word_selec.insert(INSERT, value)
    #Word_selec.tag_add("start", "1.0", END)
    #Word_selec.tag_config("start",font=("Georgia", "12", "bold"), background="yellow")
    
    inpt_str = ''.join(Txt_input.get("1.0",END))
    
    word = Txt_input.get("1.0",END)
    inpt_txt = re.sub("[^\w]", " ",  word).split()
    #print("Input_str",inpt_str)
   
    #new_str = inpt_str.replace("iterate",value)
    #Txt_input.delete(1.0,END)
    #Txt_input.insert(INSERT,inpt_str.replace("iterate",value))
    #print("New string",new_str)
    

# Words suggestion for Missing Words    

    d= DictWithPWL("en_US","Word Dicitionary4.txt")
    print(d.check(value))

    
    chk_status = d.check(value)
    
    suggst_str =  d.suggest(value)
    
    sugst_lstbx.delete(0,END)
    '''
    for sug in suggst_str:
        
        sugst_lstbx.insert(0,sug)

    #print("Sugest string",suggst_str)
        
    '''
    print("Listbox pressed")

    
def replac_word_txt(evt):
    
     sugst_word=""
     mispled_word=""
     new_inpt_str = ""
     inpt_txt     =""
     str_for_min_dis =""
     index_element =-1
     item_pos  =0

     

     value =wrd_lstbox.get(ANCHOR)
     mispled_word= Txt_Mispled_Word.get("1.0",END)
     mispled_word = mispled_word.rstrip()
     
     sugst_word =sugst_lstbx.get(ANCHOR)
     inpt_txt = Txt_input.get("1.0",END)
     
     print("Original Text",inpt_txt)

     print("lenght of mispled word",len(mispled_word))
     #new_inpt_str= inpt_txt.replace(mispled_word,sugst_word)

     

     for wdr in inpt_txt.split():
         
         #print("\n words in the text are before trimming spaces:",wdr,"  ",len(wdr))
         wdr=wdr.rstrip()
         wdr = wdr.replace(',', '')
         #print("Words after removing spaces",wdr ," ",len(wdr))

         if wdr ==  mispled_word :
            #print("There is a match")
            new_inpt_str = new_inpt_str + " " + wdr.replace(mispled_word , sugst_word) 

         else:
            new_inpt_str = new_inpt_str + " " + wdr 
            

     new_inpt_str = new_inpt_str.strip()
     
     #print("\n \n Modified String", new_inpt_str)
            

    
    

     Txt_input.delete(1.0,END)
     Txt_input.insert(INSERT,  new_inpt_str)
    
     item_pos = wrd_lstbox.get(0, END).index(mispled_word)
        
     print("Item position",    item_pos )
     wrd_lstbox.delete(item_pos)
     #wrd_lstbox.delete(mispled_word)
     
     #if  wrd_lstbox.size() ==0:
          #messagebox.showinfo("Title", "No Words Missing" )
     
     #indx_pos  = alredy_add.index(value)
     #print("Index position of deleted element",indx_pos)
     #alredy_add.pop(indx_pos)
          
    
    



def Spellchecker():
    print("\n Start time for Spell checking",str(datetime.now()))
    cnt_miss_wrd =0
    word_miss_cnt =0
    chk_status = ""
    word_tokns = ""
    word_fond = ""
    word_not_fond = ""
    strng_dict = ""
    wrd_lstbox.delete(0,END)
    word_fetc_dic = ""
    strng_gen_dict = ""
    dict_gen_arr = []
    #inpt_str = ''.join(Txt_input.get("1.0",END))
    word = Txt_input.get("1.0",END)
    #word= word.strip()
    #wordList = re.sub("[^\w]", " ",  word).split()
   
  
    print("\n Input Text " ,word )
    read_dic =""
    cnt =1
    counter =0
    word_not_fond =""
    
    fcr =  open('D:\Dicitionary.txt','r')

    for line in fcr.readlines():
        dict_gen_arr.append(line)

        

    strng_gen_dict = ' '.join(str(wrd) for wrd in dict_gen_arr)

    dw =  enchant.DictWithPWL("en_US","Dicitionary.txt")
    
    #print(" The string formed from the array",  strng_gen_dict)
   


    for w  in word.split():
       
        w = w.strip('.')
        #print ("\n Word",w )
        chk_status = dw.check(w)
        print ("\n Word",w ,"Check Status", chk_status )
        if chk_status == False:
           if  strng_gen_dict.find(w) <0 :
                cnt_miss_wrd = 1
                wrd_lstbox.insert(0,w)
              
                  
                
    if    cnt_miss_wrd <=0 : #Search For Mispelled Words in the Text : if No Mispelled Words found 
           messagebox.showinfo("Title", "No Words Missing" )   # Message Box
   
    print("\n End time for Spell checking",str(datetime.now())) 
                


   
    #print("Words not found", word_not_fond   )

def Minimu_Edit_Dist():


     leven_cost =0
     str_for_min_dist =" "
     Fnal_wrd_lst_pair =""
     lst_ocrnce = 0
     wrd_delet =""
     cur_sel =""
     emty_str_flag = 'False'
     sortlst =""
     lst_dict =""
     no_sugst_wrd = ""
     cnt_ins =0
     suggst_str_mispel_wrd =""
     cnt_minimum_edt_dist=0
     no_sugst_wrd = 'False'
     

     pos_wrd_not_fnd_dict = 0
     #Word_selec.delete(1.0,END)
     sugst_lstbx.delete(0,END)
     minm_lstbox.delete(0,END)
     Txt_Mispled_Word.delete(1.0,END)
     
     word = Txt_input.get("1.0",END)
     wordList = re.sub("[^\w]", " ",  word).split()
    
     mispled_word= Txt_Mispled_Word.get("1.0",END)
    # pos_wrd_not_fnd_dict = wrd_lstbox.get(0, END).index(mispled_word)

     
     value =wrd_lstbox.get(ANCHOR)

     Txt_Mispled_Word.insert(INSERT,value)
     Txt_Mispled_Word.tag_add("start", "1.0", END)
     Txt_Mispled_Word.tag_config("start",font=("Georgia", "12", "bold"), background="yellow")
     
     

     frdc =  open('D:Dicitionary.txt','r')

         
     value =wrd_lstbox.get(ANCHOR)
     wrd_lst_pair = " "

     
     if value == "  " or value=="" :
        emty_str_flag ="True"
        #print("Empty String has been replace",emty_str_flag)
        messagebox.showinfo("Title", "Please Select any Mispelled Words " )

     else:
        dred =  enchant.DictWithPWL("en_US","Dicitionary.txt")
        print("word selected from minimum edit distance",value)
        #dred =enchant.Dict("en_US")
        #dred = enchant.request_pwl_dict("Dicitionary.txt")
        str_for_min_dist = dred.suggest(value)

        print("String generated from Suggested Words", str_for_min_dist)
        print("Suggested Words found",dred.suggest(value),"Word",value,"String form from suggested word",str_for_min_dist)

        suggst_str_mispel_wrd = ' '.join(str(wrd) for wrd in str_for_min_dist)
        print("String found",suggst_str_mispel_wrd)
        
        no_sugst_wrd =  ' '.join(str_for_min_dist)

     if suggst_str_mispel_wrd == " " or suggst_str_mispel_wrd =="":
        emty_str_flag  = 'True'
        print("Suggested word for word not found",no_sugst_wrd,"Empty String Flag",emty_str_flag  )
        
        

       # Remove duplicate words from Suggested word fetched from the Corpus

       
       
        
    
   
     if emty_str_flag == 'False':
        for st in suggst_str_mispel_wrd.split():
           leven_cost = 0
           print("\n Suggesed Word",st)
           

           s = difflib.SequenceMatcher(None, value, st)
           print("\n The operation codes", s.get_opcodes())

           for tag, i1, i2, j1, j2 in s.get_opcodes():  #print('{:7} a[{}: {}] --> b[{}: {}] {} --> {}'.format(tag, i1, i2, j1, j2, str1[i1: i2], str2[j1: j2]))
                                                   
              
                   
               if tag == 'replace':
                   leven_cost += max(i2-i1, j2-j1)
                   
                   #wrd_lst_pair = str(leven_cost) + ":" + st + "," + wrd_lst_pair 
                   
                   #print("\n Mispelled Word", value, "Suggested Word" ,st,"leven cost", leven_cost,"Tag",tag,  i1, i2, j1, j2)

               elif tag == 'insert':
                    leven_cost += (j2-j1)
                    #wrd_lst_pair = str(leven_cost) + ":" + st + "," + wrd_lst_pair
                    cnt_minimum_edt_dist+=1

                    #print("\n Mispelled Word", value, "Suggested Word" ,st,"leven cost", leven_cost,"Tag",tag,  i1, i2, j1, j2)


               elif tag == 'delete':
                     leven_cost += (i2-i1)
                     cnt_minimum_edt_dist+=1
                     #wrd_lst_pair = str(leven_cost) + ":" + st + "," + wrd_lst_pair
                     #print("\n Mispelled Word", value, "Suggested Word" ,st,"leven cost", leven_cost,"Tag",tag, i1, i2, j1, j2)
           wrd_lst_pair = str(leven_cost) + ":" + st + "," + wrd_lst_pair
             

     #print("lenght of string ",len(wrd_lst_pair))
     

     wrd_lst_pair = wrd_lst_pair[:-1] + '/'
     wrd_lst_pair = wrd_lst_pair.rstrip(',/')
     print("\n Word and Minimum Edit Distance",  wrd_lst_pair )

 
     #print("\n Suggested Words before Entering Dicitionary",no_sugst_wrd ,emty_str_flag)
     
     if emty_str_flag  == 'True' :
        print("1")
        messagebox.showinfo("Title", "Suggested Words not found in Dicitionary" )
        #itemClicked =wrd_lstbox.get(ANCHOR) 
        #item_pos = wrd_lstbox.get(0, END).index(itemClicked)
        #print("Index Postion for which no suggested words found",item_pos)
        #wrd_lstbox.itemconfig(item_pos, bg= 'red', foreground="purple")
        add_listbox.insert(0,value)
        #frdc.write(value  + "\n")
        #messagebox.showinfo("Title","Mispelled word written successfully"  )
        #dicit_arr.append(value)

         
     
     else:
        print("2")
        for wrs in wrd_lst_pair.split(','):
            print("Suggested Words split",wrs)
            cnt_ins =0

            for rs in wrs.split(':'):
                   print("\n Pair is split",rs)

                   if cnt_ins==0:
                      bolded = font.Font(weight='bold') # will use the default font
                      minm_lstbox.config(font=bolded)
                      minm_lstbox.insert(0,rs)
                      print("Value inserted in Minimum Edit list box",rs)
                      cnt_ins = cnt_ins+1

                   else:
                        
                      bolded = font.Font(weight='bold') # will use the default font
                      sugst_lstbx.config(font=bolded)
                      print("Value inserted in Suggested box",rs)
                      sugst_lstbx.insert(0,  rs )
                      
                    
     frdc.close()
    
def Add_Dict():
    add_wrd_pos =0
    fadd =  open('D:\Dicitionary.txt','a')
    
    ad_word =add_listbox.get(ANCHOR)
    print("VAlue", ad_word )
    
    if ad_word == "  " or ad_word =="" :
        
        #print("Empty String has been replace",emty_str_flag)
         messagebox.showinfo("Title", "Please Select any Missing Words to be Added in the Dicitionary " )
    else:

         fadd.write( ad_word   + "\n")
    
         messagebox.showinfo("Title","Mispelled word written successfully"  )
         dicit_arr.append(ad_word)

         add_wrd_pos= add_listbox.get(0, END).index(ad_word)
        
         print("Item position",    add_wrd_pos )
         add_listbox.delete(add_wrd_pos)

   
     
        
#-------------------------------------------Main Application------------------------------------------------------
   
   
     
MainWindow = Tk()
MainWindow.title("Natural Language Processing")



lb1 = tkinter.Label( MainWindow, text="Enter the text to be searched in the dicitionary")

lb4 = tkinter.Label(MainWindow,text="Suggested Words")

lb_Miss_words =  tkinter.Label(MainWindow,text="Missing Words in the Dicitionary")
lb_Total_words = tkinter.Label(MainWindow,text="Total Count of Words in Corpus:")
lb_NonDuplicte_words = tkinter.Label(MainWindow,text="Non Duplicate Words:")

lb_Main_headng =   tkinter.Label(MainWindow,text="Spell Checker And Auto Correction ",font=("Georgia", "26", "bold"), fg = "black")
lb_Word_selctd_Minum_edt_Dist =  tkinter.Label(MainWindow,text="Mispelled Word:")
lbl_minm = tkinter.Label(MainWindow,text="Minimum Edit Distance:")
lble_add = tkinter.Label(MainWindow,text="Add to Dicitionary:")

f = font.Font(lb_Main_headng, lb_Main_headng.cget("font")) #To make the font underline in the Heading we have to use font class that has underline attribute
f.configure(underline=True)
lb_Main_headng.configure(font=f)


btn1 = tkinter.Button(MainWindow,text="Clear All",fg="black",command= Clear)
btn2 = tkinter.Button(MainWindow,text="Spell checker",fg="black",command= Spellchecker)
btn_load = tkinter.Button(MainWindow,text="Load file ",fg="black",command= load_file)
btn_minum_edt_dist = tkinter.Button(MainWindow,text="Minimum Edit Distance",fg="black",command= Minimu_Edit_Dist)
btn_add_dic = tkinter.Button(MainWindow,text="Add to Dicitionary",fg="black",command= Add_Dict)




Txt_input     =   Text(wrap=WORD)
sugst_lstbx   =   Listbox(MainWindow)
#Word_selec    =   Text()
wrd_lstbox    =   Listbox(MainWindow)
Txt_Totl_cnt  =   Text()
Txt_non_dupl  =   Text()
Txt_Mispled_Word =   Text()
minm_lstbox   =   Listbox(MainWindow)
add_listbox    =  Listbox(MainWindow)



lb1.place(x=50,y =180)
lb4.place(x=640,y = 190)
lb_Miss_words.place(x=420,y =190)
lb_Total_words.place(x=960,y =250)
lb_NonDuplicte_words.place(x=980,y =280)
lb_Main_headng.place(x=450,y=80)
lb_Word_selctd_Minum_edt_Dist.place(x=980,y=310)
lbl_minm.place(x=740,y = 190)
lble_add.place(x=980,y=350)


Txt_input.place(x=50,y=200,width=300,height=250)
sugst_lstbx.place(x=650,y=210,width=140,height=240)
#Word_selec.place(x=650,y=220,width=140,height=30)
wrd_lstbox.place(x=420,y=210,width=170,height=240)
minm_lstbox.place(x=790,y=210,width=40,height=240)
add_listbox.place(x=1150,y=340,width=140,height=240)

Txt_Totl_cnt.place(x=1150,y=250,width=100,height=30)
Txt_non_dupl.place(x=1150,y=280,width=100,height=30)
Txt_Mispled_Word.place(x=1150,y=310,width=140,height=30)

btn_load.place(x=50,y=480,width=100,height=60)
btn1.place(x=220,y=480,width=100,height=60)
btn2.place(x=440,y=480,width=100,height=60)
btn_minum_edt_dist.place(x=660,y=480,width=150,height=60)
btn_add_dic.place(x=1150,y=590,width=150,height=60)

Txt_input.tag_configure("center", justify='right')
Txt_input.tag_add("center", 1.0, "end")


#file_cont = pickle.load(open('D:\Word Dicitionary - Copy.txt', 'rb'))






fil_arr = []
non_duplicte =[]
dicit_arr  =[]
non_duplicte_sugst_word = []
str_for_min_dist = ""
itm_slecton =""
strng =""
set_crps = set()
set_inpt_txt = set()
global value





  
    

btn1.bind('<Button-1>', left)
wrd_lstbox.bind('<Double-Button-1>', onclick)
#wrd_lstbox.bind('<Double-Button-1>', find_sug_words)
sugst_lstbx.bind('<Double-Button-1>', replac_word_txt)

tkinter.mainloop()


