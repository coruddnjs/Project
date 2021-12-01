from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen
import requests
import json
from tkinter import *


class URL_w:
    def __init__(self,code):
        win = Tk()
        win.title("wheather")
        win.geometry("900x200")
        win.resizable(True,True)
        
        url_w = "http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation"

        self.code=code
        queryString_w = "?" + urlencode(
        {
          "serviceKey": unquote("8OPB%2BvznXm5kCbVeKjDfKYssoQ8xxC16KPlfEBz1oSOkKj7NPYoXrrkHb6M%2FF9%2FRpvEU1p5GtDhubITy%2Fo2ing%3D%3D"),
          "numOfRows" : "10",
          "pageNo" : 1,
          "dataType" : "JSON",
          "stnId" : self.code
        } 
        )

        #공공 데이터를 불러올 때 필요한 URL 조건들을 합침 
        queryURL_w=url_w+queryString_w
         
        response = requests.get(queryURL_w)
        r_dict = json.loads(response.text)
        weather=r_dict["response"]["body"]["items"]["item"]

        Date=[]
        wt=[]
        wt1=[] 
        for i in weather:
            Date.append(i["tmFc"])
            wt.append(i["wfSv1"])
            wt1.append(i["wn"])
        time=str(Date[0])
        word=wt[0]
        word1=wt1[0]
        
        total=Label(win,text=time+"\n"+word+"\n"+word1)
        total.pack()
         
        button2 =Button(win,text="종료",command=win.destroy)
        button2.pack()
         
        win.mainloop()
        
class select:

    def __init__(self,sec):
         win_S=Tk()
         win_S.title("Select")
         win_S.geometry("900x500")
         win_S.resizable(True,True)
         
         S=["서울","인천","수원","성남","안양","광명","과천","평택","오산"]
         S_code=["11B10101","11B20201","11B20601","11B20605","11B20602",
                 "11B10103","11B10102","11B20606","11B20603"]
         
         B=["부산","울산","김해","창원","진주","통영","사천","고성","남해"]
         B_code=["11H20201","11H20101","11H20304","11H20301","11H20701",
                 "11H20401","11H20402","11H20404","11H20405"]

         D=["대구","영천","경산","청도","칠곡","구미","고령","울릉도","독도"]
         D_code=["11H10701","11H10702","11H10703","11H10704","11H10705",
                 "11H10602","11H10604","11E00101","11E00102"]

         G=["광주","나주","장성","담양","목포","진도","순천","곡성","고흥"]
         G_code=["11F20501","11F20503","11F20502","11F20504","21F20801",
                 "21F20201","11F20603","11F20602","11F20403"]

         J=["전주","익산","군산","정읍","김제","남원","고창","무주","부안"]
         J_code=["11F10201","11F10202","21F10501","11F10203","21F10502",
                 "11F10401","21F10601","11F10302","21F10602"]

         C_S=["대전","세종","공주","논산","계룡","금산","천안","아산","서산"]
         C_S_code=["11C20401","11C20404","11C20402","11C20602","11C20403",
                 "11C20601","11C20301","11C20302","11C20101"]

         C_N=["청주","증평","괴산","진천","충주","음성","제천","단양","보은"]
         C_N_code=["11C10301","11C10304","11C10303","11C10102","11C10101",
                 "11C10103","11C10201","11C10202","11C10302"]

         Gang=["철원","화천","인제","양구","춘천","홍천","원주","횡성","평창"]
         Gang_code=["11D10101","11D10102","11D10201","11D10202","11D10301",
                 "11D10302","11D10401","11D10402","11D10503"]

         Jeju=["제주","서귀포","성산","고산","성판악","이어도","추자도"]
         Jeju_code=["11G00201","11G00401","11G00101","11G00501","11G00302",
                 "11G00601","11G00800"]
         
         if(sec=="서울.인천.경기도"):
             button=Button(win_S,width=10,height=10,text=S[0],command=lambda:self.exer(S_code[0],S[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=S[1],command=lambda:self.exer(S_code[1],S[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=S[2],command=lambda:self.exer(S_code[2],S[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=S[3],command=lambda:self.exer(S_code[3],S[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=S[4],command=lambda:self.exer(S_code[4],S[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=S[5],command=lambda:self.exer(S_code[5],S[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=S[6],command=lambda:self.exer(S_code[6],S[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=S[7],command=lambda:self.exer(S_code[7],S[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=S[8],command=lambda:self.exer(S_code[8],S[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="부산.울산.경상남도"):
             button=Button(win_S,width=10,height=10,text=B[0],command=lambda:self.exer(B_code[0],B[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=B[1],command=lambda:self.exer(B_code[1],B[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=B[2],command=lambda:self.exer(B_code[2],B[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=B[3],command=lambda:self.exer(B_code[3],B[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=B[4],command=lambda:self.exer(B_code[4],B[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=B[5],command=lambda:self.exer(B_code[5],B[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=B[6],command=lambda:self.exer(B_code[6],B[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=B[7],command=lambda:self.exer(B_code[7],B[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=B[8],command=lambda:self.exer(B_code[8],B[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="대구.경상북도"):
             button=Button(win_S,width=10,height=10,text=D[0],command=lambda:self.exer(D_code[0],D[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=D[1],command=lambda:self.exer(D_code[1],D[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=D[2],command=lambda:self.exer(D_code[2],D[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=D[3],command=lambda:self.exer(D_code[3],D[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=D[4],command=lambda:self.exer(D_code[4],D[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=D[5],command=lambda:self.exer(D_code[5],D[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=D[6],command=lambda:self.exer(D_code[6],D[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=D[7],command=lambda:self.exer(D_code[7],D[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=D[8],command=lambda:self.exer(D_code[8],D[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="광주.전라남도"):
             button=Button(win_S,width=10,height=10,text=G[0],command=lambda:self.exer(G_code[0],G[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=G[1],command=lambda:self.exer(G_code[1],G[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=G[2],command=lambda:self.exer(G_code[2],G[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=G[3],command=lambda:self.exer(G_code[3],G[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=G[4],command=lambda:self.exer(G_code[4],G[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=G[5],command=lambda:self.exer(G_code[5],G[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=G[6],command=lambda:self.exer(G_code[6],G[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=G[7],command=lambda:self.exer(G_code[7],G[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=G[8],command=lambda:self.exer(G_code[8],G[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="전라북도"):
             button=Button(win_S,width=10,height=10,text=J[0],command=lambda:self.exer(J_code[0],J[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=J[1],command=lambda:self.exer(J_code[1],J[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=J[2],command=lambda:self.exer(J_code[2],J[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=J[3],command=lambda:self.exer(J_code[3],J[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=J[4],command=lambda:self.exer(J_code[4],J[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=J[5],command=lambda:self.exer(J_code[5],J[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=J[6],command=lambda:self.exer(J_code[6],J[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=J[7],command=lambda:self.exer(J_code[7],J[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=J[8],command=lambda:self.exer(J_code[8],J[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="대전.세종.충청남도"):
             button=Button(win_S,width=10,height=10,text=C_S[0],command=lambda:self.exer(C_S_code[0],C_S[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=C_S[1],command=lambda:self.exer(C_S_code[1],C_S[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=C_S[2],command=lambda:self.exer(C_S_code[2],C_S[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=C_S[3],command=lambda:self.exer(C_S_code[3],C_S[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=C_S[4],command=lambda:self.exer(C_S_code[4],C_S[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=C_S[5],command=lambda:self.exer(C_S_code[5],C_S[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=C_S[6],command=lambda:self.exer(C_S_code[6],C_S[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=C_S[7],command=lambda:self.exer(C_S_code[7],C_S[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=C_S[8],command=lambda:self.exer(C_S_code[8],C_S[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="충청북도"):
             button=Button(win_S,width=10,height=10,text=C_N[0],command=lambda:self.exer(C_N_code[0],C_N[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=C_N[1],command=lambda:self.exer(C_N_code[1],C_N[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=C_N[2],command=lambda:self.exer(C_N_code[2],C_N[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=C_N[3],command=lambda:self.exer(C_N_code[3],C_N[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=C_N[4],command=lambda:self.exer(C_N_code[4],C_N[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=C_N[5],command=lambda:self.exer(C_N_code[5],C_N[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=C_N[6],command=lambda:self.exer(C_N_code[6],C_N[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=C_N[7],command=lambda:self.exer(C_N_code[7],C_N[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=C_N[8],command=lambda:self.exer(C_N_code[8],C_N[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="강원도"):
             button=Button(win_S,width=10,height=10,text=Gang[0],command=lambda:self.exer(Gang_code[0],Gang[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=Gang[1],command=lambda:self.exer(Gang_code[1],Gang[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=Gang[2],command=lambda:self.exer(Gang_code[2],Gang[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=Gang[3],command=lambda:self.exer(Gang_code[3],Gang[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=Gang[4],command=lambda:self.exer(Gang_code[4],Gang[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=Gang[5],command=lambda:self.exer(Gang_code[5],Gang[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=Gang[6],command=lambda:self.exer(Gang_code[6],Gang[6]))
             button6.pack(side=LEFT)
             button7=Button(win_S,width=10,height=10,text=Gang[7],command=lambda:self.exer(Gang_code[7],Gang[7]))
             button7.pack(side=LEFT)
             button8=Button(win_S,width=10,height=10,text=Gang[8],command=lambda:self.exer(Gang_code[8],Gang[8]))
             button8.pack(side=LEFT)
             
         elif(sec=="제주도"):
             button=Button(win_S,width=10,height=10,text=Jeju[0],command=lambda:self.exer(Jeju_code[0],Jeju[0]))
             button.pack(side=LEFT)
             button1=Button(win_S,width=10,height=10,text=Jeju[1],command=lambda:self.exer(Jeju_code[1],Jeju[1]))
             button1.pack(side=LEFT)
             button2=Button(win_S,width=10,height=10,text=Jeju[2],command=lambda:self.exer(Jeju_code[2],Jeju[2]))
             button2.pack(side=LEFT)
             button3=Button(win_S,width=10,height=10,text=Jeju[3],command=lambda:self.exer(Jeju_code[3],Jeju[3]))
             button3.pack(side=LEFT)
             button4=Button(win_S,width=10,height=10,text=Jeju[4],command=lambda:self.exer(Jeju_code[4],Jeju[4]))
             button4.pack(side=LEFT)
             button5=Button(win_S,width=10,height=10,text=Jeju[5],command=lambda:self.exer(Jeju_code[5],Jeju[5]))
             button5.pack(side=LEFT)
             button6=Button(win_S,width=10,height=10,text=Jeju[6],command=lambda:self.exer(Jeju_code[6],Jeju[6]))
             button6.pack(side=LEFT)
             
             
         button2 =Button(win_S,width=5,height=5,text="종료",command=win_S.destroy)
         button2.pack(side=BOTTOM)

         win_S.mainloop()
    
    def exer(self,region,se):
        URL(region,se)
        
class URL:
    
    def __init__(self,region,sec):
         win_U = Tk()
         win_U.title("wheather")
         win_U.geometry("1000x500")
         win_U.resizable(True,True)
         self.sec=sec
         self.region=region ##지역 코드를 받기 위해 초기화시켜준다.
         
         #공공 API(주소)에서 데이터 가지고 오기 기본
         url = "http://apis.data.go.kr/1360000/VilageFcstMsgService/getLandFcst"

         queryString = "?" + urlencode(
         {
           "serviceKey": unquote("8OPB%2BvznXm5kCbVeKjDfKYssoQ8xxC16KPlfEBz1oSOkKj7NPYoXrrkHb6M%2FF9%2FRpvEU1p5GtDhubITy%2Fo2ing%3D%3D"),
           "numOfRows" : "1",
           "pageNo" : 1,
           "dataType" : "JSON",
           "regId" : self.region
         } 
         )
         queryURL = url + queryString

         response = requests.get(queryURL)
         r_dict = json.loads(response.text)
         weather=r_dict["response"]["body"]["items"]["item"]

         Date=[]
         wt=[]
         ta=[]
         wd=[]
         ra=[]
         
         photo_img=[PhotoImage(file="so.png",master=win_U),
                PhotoImage(file="crow.png",master=win_U),
                PhotoImage(file="rain.png",master=win_U),
                PhotoImage(file="sun.png",master=win_U),
                PhotoImage(file="snow.png",master=win_U)]
     
         for i in weather:
              Date.append(i["announceTime"])
              wt.append(i["wf"])
              ta.append(i["ta"])
              wd.append(i["wd1"])
              ra.append(i["rnSt"])

         word=wt[0]
         time=str(Date[0])
         temp=str(ta[0])
         wind=wd[0]
         rain=(str(ra[0]))
         
         f = open("C:\Desktop\전공과제\창업프로젝트\past_weather.txt","a")
         f.write(self.sec+" ")
         f.write(time+" ")
         f.write(word+" ")
         f.write(temp+"C"+" ")
         f.write(wind+" ")
         f.write(rain+"%"+"\n")
         f.close()
         
         if ("흐림" in word):
              photo=photo_img[0]
              wt=Label(win_U,image=photo)
              wt.pack(side=LEFT)
              wt1=Label(win_U,text="지역: "+self.sec+"\n발표 시간: "+ time+"\n"+"날씨 :"
                        + word+"\n"+"기온 : "+temp+"C\n"+"풍향 :"+wind+"\n강수확률 :"+rain+"%")
              wt1.pack(side=LEFT)
         elif ("구름많음" in word):
              photo=photo_img[1]
              wt=Label(win_U,image=photo)
              wt.pack(side=LEFT)
              wt1=Label(win_U,text="지역: "+self.sec+"\n발표 시간: "+time+"\n"+"날씨 :"
                        +word+"\n"+"기온 : "+ temp +"C\n풍향 :"+wind+"\n강수확률 :"+rain+"%")
              wt1.pack(side=LEFT)
         elif ("맑음" in word):  
              photo=photo_img[3] 
              wt=Label(win_U,image=photo)
              wt.pack(side=LEFT)
              wt1=Label(win_U,text="지역: "+self.sec+"\n발표 시간: "+time+"\n"+"날씨 :"
                        +word+"\n"+"기온 : "+temp+"C\n풍향 :"+wind+"\n강수확률 :"+rain+"%")
              wt1.pack(side=LEFT)
         elif ("비" in word):
              photo=photo_img[2]
              wt=Label(win_U,image=photo)
              wt.pack(side=LEFT)
              wt1=Label(win_U,text="지역: "+self.sec+"\n발표 시간:"+time+"\n"+"날씨 :"
                        + word+"\n"+"기온 : "+temp+"C\n풍향 :"+wind+"\n강수확률 :"+rain+"%")
              wt1.pack(side=LEFT)
         elif ("눈" in word):
              photo=photo_img[4]
              wt=Label(win_U,image=photo)
              wt.pack(side=LEFT)
              wt1=Label(win_U,text="지역: "+self.sec+"\n발표 시간: "+time+"\n"+"날씨 :"
                        +word+"\n"+"기온 : "+temp+"C\n풍향 :"+wind+"\n강수확률 :"+rain+"%")
              wt1.pack(side=LEFT)
        
         wt1.config(font=("Arial",20))
         button2 =Button(win_U,width=15,height=10,text="종료",command=win_U.destroy)
         button2.pack(side=BOTTOM)
         
         win_U.mainloop()
         
class Select:
    

    def __init__(self):
        win=Tk()
        win.title("Select")
        win.geometry("1100x500")
        List=["서울.인천.경기도","부산.울산.경상남도","대구.경상북도","광주.전라남도",
               "전라북도","대전.세종.충청남도","충청북도","강원도","제주도"]
       
        button=Button(win,width=15,height=15,text=List[0],command=lambda:self.exe(List[0]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[1],command=lambda:self.exe(List[1]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[2],command=lambda:self.exe(List[2]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[3],command=lambda:self.exe(List[3]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[4],command=lambda:self.exe(List[4]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[5],command=lambda:self.exe(List[5]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[6],command=lambda:self.exe(List[6]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[7],command=lambda:self.exe(List[7]))
        button.pack(side=LEFT)
        button=Button(win,width=15,height=15,text=List[8],command=lambda:self.exe(List[8]))
        button.pack(side=LEFT)
         
        button2 =Button(win,width=10,height=10,text="종료",command=win.destroy) 
        button2.pack(side=BOTTOM)
        
        win.mainloop()
 
    def exe(self,sec):
        select(sec)
            

class search():
    
     def __init__(self):
        self.win=Tk()
        self.win.title("Search")
        self.win.geometry("1000x500")
        self.E=Entry(self.win)
        self.E.grid(row=0,column=0)
        self.E2=Entry(self.win)
        self.E2.grid(row=0,column=1)
        ex1=Label(self.win,text="날짜: 20211129")
        ex2=Label(self.win,text="지역: 청주")
        ex1.grid(row=1,column=0)
        ex2.grid(row=1,column=1)
        button=Button(self.win,text="입력",command=self.searchs)
        button.grid(row=2,column=0)
        button1=Button(self.win,text="전체날씨검색(히스토리)",command=self.ALL_search)
        button1.grid(row=2,column=1)
        Backbutton=Button(self.win,text="종료",command=self.win.destroy)
        Backbutton.grid(row=3,column=0)
        label=Label(self.win,text="번호  지역    날짜    날씨상태   기온   풍향   강수량")
        label.grid(row=0,column=3)
        label2=Label(self.win,text="번호  지역    날짜    날씨상태   기온   풍향   강수량")
        label2.grid(row=0,column=4)
        self.win.mainloop()
    
     def searchs(self):
         with open("C:\Desktop\전공과제\창업프로젝트\past_weather.txt","r") as f:
             count=0
             lines=f.readlines()
             for i in lines:
                 if(self.E.get() in i and self.E2.get() in i):
                        self.labelcount=Label(self.win,width=50)
                        self.labelcount.grid(row=count+1,column=3)
                        self.labelcount.config(text=str(count+1)+"."+i)
                        count=count+1
            
     def ALL_search(self):
         with open("C:\Desktop\전공과제\창업프로젝트\past_weather.txt","r") as f:
             count=0
             lines=f.readlines()
             for i in lines:
                 self.labelcount=Label(self.win,width=50)
                 self.labelcount.grid(row=count+1,column=4)
                 self.labelcount.config(text=str(count+1)+"."+i)
                 count=count+1
                  

class MAIN:

    def __init__(self):
        window=Tk()
        window.title("Wheather")
        window.geometry("640x400+100+100")
        window.resizable(True,True)
        
        label=Label(window,text="API를 이용한 날씨예보 프로그램",font=("궁서체",20),fg="red")
        label.pack(side=TOP)
        button =Button(window,width=15,height=10,text="지역선택",command=self.exe)
        button.pack(side=LEFT)

        button1 =Button(window,width=15,height=10,text="전국기상개황",command=self.exes)
        button1.pack(side=LEFT)

        button3=Button(window,width=15,height=10,text="날씨 검색",command=self.search_s)
        button3.pack(side=LEFT)
        
        button2 =Button(window,width=15,height=10,text="종료",command=window.destroy)
        button2.pack(side=LEFT)

        window.mainloop()

    def exe(self):
        Select()

    def exes(self):
        URL_w("108")

    def search_s(self):
        search()

MAIN()     


