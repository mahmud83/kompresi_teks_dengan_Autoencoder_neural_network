<<<<<<< HEAD
from tkinter import filedialog
from tkinter import *
import random
import time;
import sys
import random
import numpy as np




root =Tk()
root.geometry("1600x700+0+0")
root.title("Kompresi Data Teks dengan Auto Encoder Neural Network")

Tops = Frame(root, width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=LEFT)

lblInfo = Label(Tops, font=('arial',36,'bold'),text="Kompresi Data Teks dengan Auto Encoder Neural Network",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=0,columnspan=10)

#----------------KOLOM 1-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="Oleh M Nur Alfiansyah",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=1,columnspan=10)

#----------------KOLOM 2-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=2,columnspan=10)

#----------------KOLOM 3-------------------------------------------#
lblInfo = Label(Tops, width=10,font=('arial',20,'bold'),text="Masukan file...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=3,column=0)

btn7=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="Pilih File",bg="powder blue",command=lambda: btnClick())
btn7.grid(row=3,column=2)

btn8=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="KOMPRESI",bg="powder blue",command=lambda: btnKompres())
btn8.grid(row=3,column=4)

lblInfo = Label(Tops, font=('arial',20,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=3,column=5)

btn9=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="DEKOMPRESI",bg="powder blue",command=lambda: btnDekompres())
btn9.grid(row=3,column=6)

#----------------KOLOM 4-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=4,columnspan=10)

#----------------KOLOM 5-------------------------------------------#


#----------------KOLOM 6-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=6,columnspan=10)

#----------------KOLOM 7-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=7,columnspan=10)

#----------------KOLOM 8-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=8,columnspan=10)

lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=9,columnspan=10)

lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=10,columnspan=10)


#letak fungsi
def btnClick():
    root.fileName = filedialog.askopenfilename(filetypes = ((" ",".txt"),("All files","*")))
    lblInfo = Label(Tops, font=('arial',20,'bold'),text=root.fileName,fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=2,columnspan=5)

def btnKompres():
    lblInfo = Label(Tops, font=('arial',30,'bold'),text=".....PLEASE WAIT...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    files = open(root.fileName,'r')
    isi_teks = files.read()

    #print(isi_teks)
    #------------------------------------------------------------------------------

    #KONVERSI DARI KARAKTER KE ASCII
    #------------------------------------------------------------------------------
    isi_teks_desimal = []
    for i in range(len(isi_teks)):
        isi_teks_desimal.append(str(ord(isi_teks[i])))
    #------------------------------------------------------------------------------


    #NORMALISASI
    #------------------------------------------------------------------------------
    N_isi_teks = []
    for i in range(len(isi_teks_desimal)):
        Nteks = 0
        Nteks = int(isi_teks_desimal[i]) - 32
        Nteks = Nteks / 122
        # Nteks = Nteks*1e-01
        N_isi_teks.append(Nteks)
    N_isi_teksS = np.transpose(np.matrix(N_isi_teks))
    N_isi_teks = np.matrix(np.transpose(np.matrix(N_isi_teks)))
    #------------------------------------------------------------------------------

    #MENGHITUNG BANYAKNYA JUMLAH HIDDEN LAYER 1, HIDDEN LAYER 2
    #------------------------------------------------------------------------------
    pembagiHidden = 4
    nHiddenLayer1 = round(int(len(N_isi_teks)) / int(pembagiHidden))
    #------------------------------------------------------------------------------

    #INISIASI PEMBOBOT
    #------------------------------------------------------------------------------
    W = np.random.uniform(0,len(isi_teks)**.5,(nHiddenLayer1,len(isi_teks)))*1e-1
    W = np.matrix(W)




    B1 = np.random.uniform(0,len(isi_teks)**.5,(nHiddenLayer1,1))*1e-5
    B1 = np.reshape(B1,(nHiddenLayer1,1))
    # print(B1)


    V = np.random.uniform(0,nHiddenLayer1**.5,(len(isi_teks),nHiddenLayer1))*1e-1
    V = np.matrix(V)


    B2 = np.random.uniform(0,nHiddenLayer1**.5,(len(isi_teks),1))*1e-5
    B2 = np.reshape(B2,(len(isi_teks),1))

    #------------------------------------------------------------------------------

    #INISIASI TARGET ERROR,E,ALPA,MOMENTUM,ITERASI
    #------------------------------------------------------------------------------
    TargetError = 1e-5
    Error = 1
    Alpa = 0.7
    Iter = 0
    momentum = 1
    E = 1;

    t = np.zeros((len(isi_teks_desimal),1))

    # print(int(isi_teks_desimal[1])/2)
    for i in range(len(isi_teks_desimal)):
        t[i] = int(isi_teks_desimal[i]) / 122
    #------------------------------------------------------------------------------

    # print(t)
    #PELATIHAN
    #------------------------------------------------------------------------------
    # h=np.matrix([])
    h = np.zeros(nHiddenLayer1)
    dV = np.zeros(nHiddenLayer1*len(isi_teks))
    dV = np.reshape(dV,(len(isi_teks),nHiddenLayer1))

    simpanV ='' #np.zeros(np.size(V))



    dEy = np.zeros(len(isi_teks_desimal))
    dEy = np.reshape(dEy,(len(isi_teks),1))

    y = np.zeros(len(isi_teks_desimal))

    deltaW = np.zeros(nHiddenLayer1*len(isi_teks))
    deltaW = np.reshape(deltaW,(nHiddenLayer1,len(isi_teks)))

    c= []
    cc = 0
    while E>TargetError:
    # while Iter<1:
        Iter = Iter +1
        for n in range(1):
            # print(W)
            #HIDDEN LAYER 1
            #-----------------------------------------------------------------------
            c = W*N_isi_teks+B1
            for i in range(nHiddenLayer1):
                h[i]= ((2/(1+np.exp((-2*-c[i])))))
            h = np.reshape(h,(nHiddenLayer1,1))
            #-----------------------------------------------------------------------

            #HIDDEN LAYER 2
            #----------------------------------------------------------------------

            yy = V*h+B2
            for i in range(len(isi_teks)):
                y[i]= ((2/(1+np.exp((-2*-y[i])))))
            y = yy
            #----------------------------------------------------------------------

            #---------------------------------------------------------------------

              ##########################
             ###------BACKWARD------###
            ##########################


            #ERROR NET
            #-----------------------------------------------------------------------


            e = -(np.matrix(y) - np.matrix(t))

            for i in range(len(isi_teks)):
                dEy[i] = e[i] * y[i] * (1-y[i])


            dH = np.transpose(V)*dEy


            for i in range(len(isi_teks)): #untuk baris
                for j in range(nHiddenLayer1):
                    dV[i,j] = dEy[i] * h[j]

            # print(W)
            for i in range(nHiddenLayer1): #untuk baris
                for j in range(len(isi_teks)):
                    deltaW[i,j] = dH[i] * N_isi_teks[j]

            #UPDATE PEMBOBOT
            #----------------------------------------------------------------------
            W  = (momentum * W)+(deltaW * Alpa)

            B1 = momentum * B1 + dH * Alpa


            V  = momentum * V  +  dV * Alpa

            B2 = momentum * B2 + dEy * Alpa

            #-----------------------------------------------------------------------

        E=np.sum(0.5 * (np.power(e,2)))
        #print(h)
        #print(y)
        print('ITERASI ke -',Iter,' || Error =',E)
    #----------------------------------------------------------------------- --------

    ################################################################################
    #---------------PROSES KOMPRESI DENGAN VARIABEL HIDDEN LAYER-------------------#
    ################################################################################
    c = W*N_isi_teks+B1
    for i in range(nHiddenLayer1):
        h[i]= ((2/(1+np.exp((-2*-c[i])))))
    h = np.reshape(h,(nHiddenLayer1,1))

    # print(h)

    #-------------------------------------------------------------------------------
    #menyimpan pembobot v
    file_v = open("pembobot/pembobotV.txt","w")
    # print(np.size(V,1))

    iterasiK=0;
    iterasiB=0;
    for i in range(np.size(V)):

        if np.mod(i,np.size(V,1))==0:
            iterasiK=0
            iterasiB=iterasiB+1

        # simpanV.append(" ",V[iterasiB-1,iterasiK])
        simpanV = simpanV+"{0} ".format(V[iterasiB-1,iterasiK])
        # print(V[iterasiB-1,iterasiK])
        # isi_teks_desimal.append(str(ord(isi_teks[i])))

        # print("K= ",iterasiK,"| B = ",iterasiB-1,"| i= ",i)
        iterasiK=iterasiK+1
    # A=[0.001 0.002]



    file_v.write(str(simpanV))
    file_v.close()

    #menyimpan ukuran W
    #print(V)
    file_v = open("pembobot/sizeV.txt","w")
    ukuran = "{0} {1}".format(np.size(V,0),np.size(V,1))
    file_v.write(ukuran)
    file_v.close()


    #menyimpan pembobot b
    ################################################################################
    file_v = open("pembobot/pembobotB.txt","w")
    # print(np.size(V,1))

    iterasiK=0;
    iterasiB=0;
    simpanB2=''
    for i in range(np.size(B2)):

        if np.mod(i,np.size(B2,1))==0:
            iterasiK=0
            iterasiB=iterasiB+1

        # simpanV.append(" ",V[iterasiB-1,iterasiK])
        simpanB2 = simpanB2+"{0} ".format(B2[iterasiB-1,iterasiK])
        # print(V[iterasiB-1,iterasiK])
        # isi_teks_desimal.append(str(ord(isi_teks[i])))

        # print("K= ",iterasiK,"| B = ",iterasiB-1,"| i= ",i)
        iterasiK=iterasiK+1
    # A=[0.001 0.002]



    file_v.write(str(simpanB2))
    file_v.close()


    #menyimpan ukuran W
    ukuran=''
    file_v = open("pembobot/sizeB2.txt","w")
    ukuran = "{0} {1}".format(np.size(B2,0),np.size(B2,1))
    file_v.write(ukuran)
    file_v.close()


    ################################################################################
    # hasil_normalisasi = np.zeros((nHiddenLayer1,1))
    #
    # maksimal_hasil_normalisasi = np.max(h)
    # minimal_hasil_normalisasi = np.min(h)
    # for i in range(nHiddenLayer1):
    #     hasil_normalisasi[i]=np.round((h[i] - minimal_hasil_normalisasi) / (maksimal_hasil_normalisasi-minimal_hasil_normalisasi)*190)


    #simapn maks and min
    maksimal_hasil_normalisasi = np.max(h)
    minimal_hasil_normalisasi = np.min(h)

    minmaks = '{0} {1}'.format(maksimal_hasil_normalisasi,minimal_hasil_normalisasi)
    file_v = open("pembobot/minmaks.txt","w")
    file_v.write(minmaks)
    file_v.close()
    #uvah ke char

    teks_hasil_kompresi=''
    for i in range(nHiddenLayer1):
        teks_hasil_kompresi=teks_hasil_kompresi+'{0}'.format(chr((np.round((h[i] - minimal_hasil_normalisasi) / (maksimal_hasil_normalisasi-minimal_hasil_normalisasi)*113))+14))

    #menyimpan hasil kompresi
    file_v = open("hasilkompresi.txt","w")
    file_v.write(teks_hasil_kompresi)
    file_v.close()

    #print('Hasil kompresi')
    #print(h)


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       SUCCESS          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="                                          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="_______________________________________________",fg="red",bd=10,anchor='w',bg="powder blue")


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       Hasil Kompresi          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',8,'bold'),text=teks_hasil_kompresi,fg="red",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=9,columnspan=10)




#-------------------------------------------------------------------------------------------
def btnDekompres():
    lblInfo = Label(Tops, font=('arial',30,'bold'),text=".....PLEASE WAIT...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    files = open(root.fileName,'r')
    hasil = files.read()
    kata = []

    iter1=0
    for i in range(len(hasil)):
        iter1=iter1+1
        kata.append(ord(hasil[i]))


    dV= np.zeros(iter1)
    h = np.reshape(dV,(iter1,1))


    files = open('pembobot/minmaks.txt','r')
    minmaks = files.read()
    minmaks1 = minmaks.split(' ')
    #ambil maksimal
    maksimal_hasil_normalisasi = float(minmaks1[0])

    #ambil minimal
    minimal_hasil_normalisasi = float(minmaks1[1])
    files.close()

    for i in range(iter1):
        #print(i,'|iterasi|',iter1)
        h[i]=((((maksimal_hasil_normalisasi - minimal_hasil_normalisasi)/113)*kata[i])+minimal_hasil_normalisasi)

    # print(h)
    h=np.matrix(h)
    #print(np.size(h),'||',np.size(kata))

    #membuka file pembobot V
    #-------------------------------------------------------------------------------
    files = open('pembobot/pembobotV.txt','r')
    kalimat = files.read()
    kata = kalimat.split(' ')

    for i in range(len(kata)-1):
        kata[i]=float(kata[i])

    files = open('pembobot/sizeV.txt','r')
    sizeV = files.read()
    sizeV = sizeV.split(' ')

    dV = np.zeros(int(sizeV[0])*int(sizeV[1]))
    V = np.reshape(dV,(int(sizeV[0]),int(sizeV[1])))

    iterasiK=0
    iterasiB=0
    for i in range(len(kata)-1):
        V[iterasiB,iterasiK]=kata[i]
        iterasiK=iterasiK+1

        if np.mod(iterasiK,int(sizeV[1]))==0:
            iterasiK=0
            iterasiB=iterasiB+1

    V=np.matrix(V)

    #membuka file pembobot B
    #-------------------------------------------------------------------------------
    files = open('pembobot/pembobotB.txt','r')
    kalimatB = files.read()
    kata = kalimatB.split(' ')

    for i in range(len(kata)-1):
        kata[i]=float(kata[i])

    files = open('pembobot/sizeB2.txt','r')
    sizeB2 = files.read()
    sizeB2 = sizeB2.split(' ')

    dB2 = np.zeros(int(sizeB2[0])*int(sizeB2[1]))
    B2 = np.reshape(dB2,(int(sizeB2[0]),int(sizeB2[1])))

    iterasiK=0
    iterasiB=0
    for i in range(len(kata)-1):
        B2[iterasiB,iterasiK]=kata[i]
        iterasiK=iterasiK+1

        if np.mod(iterasiK,int(sizeB2[1]))==0:
            iterasiK=0
            iterasiB=iterasiB+1

    B2=np.matrix(B2)


    #PROSES dekompresi
    #===========
    y = np.zeros(int(sizeB2[0]))
    #print(np.size(V),'||',np.size(V))
    yy = V*h+B2
    for i in range(int(sizeB2[0])):
        y[i]= ((2/(1+np.exp((-2*-y[i])))))
    y = yy


    #-----------
    hasil_akhir = y * 122
    # hasil_akhir = np.round(hasil_akhir,2)
    # print(hasil_akhir)

    ##KONVERSI
    hasil_kata=""
    for i in range(len(hasil_akhir)):
        xyz=hasil_akhir[i]-np.round(hasil_akhir[i],0)

        if xyz>=0.5:
            hasil_akhir[i]=hasil_akhir[i]
        else:
            if (xyz-0.4)>=0.05:
                hasil_akhir[i] = hasil_akhir[i]+0.1
            else:
                hasil_akhir[i]=hasil_akhir[i]

    ##KONVERSI
    hasil_kata=""
    for i in range(len(hasil_akhir)):
        # print(chr(np.round(hasil_akhir[i]))," || ",hasil_akhir[i])
        hasil_kata = hasil_kata + chr(np.round(hasil_akhir[i]))


    file_v = open("hasilDekompresi.txt","w")
    file_v.write(hasil_kata)
    file_v.close()





    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       SUCCESS          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="                                          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="_______________________________________________",fg="red",bd=10,anchor='w',bg="powder blue")


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       Hasil Dekompresi          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',8,'bold'),text=hasil_kata,fg="red",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=9,columnspan=10)




root.mainloop()
=======
from tkinter import filedialog
from tkinter import *
import random
import time;
import sys
import random
import numpy as np




root =Tk()
root.geometry("1600x700+0+0")
root.title("Kompresi Data Teks dengan Auto Encoder Neural Network")

Tops = Frame(root, width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=LEFT)

lblInfo = Label(Tops, font=('arial',36,'bold'),text="Kompresi Data Teks dengan Auto Encoder Neural Network",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=0,columnspan=10)

#----------------KOLOM 1-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="Oleh M Nur Alfiansyah",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=1,columnspan=10)

#----------------KOLOM 2-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=2,columnspan=10)

#----------------KOLOM 3-------------------------------------------#
lblInfo = Label(Tops, width=10,font=('arial',20,'bold'),text="Masukan file...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=3,column=0)

btn7=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="Pilih File",bg="powder blue",command=lambda: btnClick())
btn7.grid(row=3,column=2)

btn8=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="KOMPRESI",bg="powder blue",command=lambda: btnKompres())
btn8.grid(row=3,column=4)

lblInfo = Label(Tops, font=('arial',20,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=3,column=5)

btn9=Button(Tops,padx=16,pady=16,bd=8,fg="yellow",font=('arial',15,'bold'),text="DEKOMPRESI",bg="powder blue",command=lambda: btnDekompres())
btn9.grid(row=3,column=6)

#----------------KOLOM 4-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=4,columnspan=10)

#----------------KOLOM 5-------------------------------------------#


#----------------KOLOM 6-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=6,columnspan=10)

#----------------KOLOM 7-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=7,columnspan=10)

#----------------KOLOM 8-------------------------------------------#
lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=8,columnspan=10)

lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=9,columnspan=10)

lblInfo = Label(Tops, font=('arial',30,'bold'),text="",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
lblInfo.grid(row=10,columnspan=10)


#letak fungsi
def btnClick():
    root.fileName = filedialog.askopenfilename(filetypes = ((" ",".txt"),("All files","*")))
    lblInfo = Label(Tops, font=('arial',20,'bold'),text=root.fileName,fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=2,columnspan=5)

def btnKompres():
    lblInfo = Label(Tops, font=('arial',30,'bold'),text=".....PLEASE WAIT...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    files = open(root.fileName,'r')
    isi_teks = files.read()

    #print(isi_teks)
    #------------------------------------------------------------------------------

    #KONVERSI DARI KARAKTER KE ASCII
    #------------------------------------------------------------------------------
    isi_teks_desimal = []
    for i in range(len(isi_teks)):
        isi_teks_desimal.append(str(ord(isi_teks[i])))
    #------------------------------------------------------------------------------


    #NORMALISASI
    #------------------------------------------------------------------------------
    N_isi_teks = []
    for i in range(len(isi_teks_desimal)):
        Nteks = 0
        Nteks = int(isi_teks_desimal[i]) - 32
        Nteks = Nteks / 122
        # Nteks = Nteks*1e-01
        N_isi_teks.append(Nteks)
    N_isi_teksS = np.transpose(np.matrix(N_isi_teks))
    N_isi_teks = np.matrix(np.transpose(np.matrix(N_isi_teks)))
    #------------------------------------------------------------------------------

    #MENGHITUNG BANYAKNYA JUMLAH HIDDEN LAYER 1, HIDDEN LAYER 2
    #------------------------------------------------------------------------------
    pembagiHidden = 4
    nHiddenLayer1 = round(int(len(N_isi_teks)) / int(pembagiHidden))
    #------------------------------------------------------------------------------

    #INISIASI PEMBOBOT
    #------------------------------------------------------------------------------
    W = np.random.uniform(0,len(isi_teks)**.5,(nHiddenLayer1,len(isi_teks)))*1e-1
    W = np.matrix(W)




    B1 = np.random.uniform(0,len(isi_teks)**.5,(nHiddenLayer1,1))*1e-5
    B1 = np.reshape(B1,(nHiddenLayer1,1))
    # print(B1)


    V = np.random.uniform(0,nHiddenLayer1**.5,(len(isi_teks),nHiddenLayer1))*1e-1
    V = np.matrix(V)


    B2 = np.random.uniform(0,nHiddenLayer1**.5,(len(isi_teks),1))*1e-5
    B2 = np.reshape(B2,(len(isi_teks),1))

    #------------------------------------------------------------------------------

    #INISIASI TARGET ERROR,E,ALPA,MOMENTUM,ITERASI
    #------------------------------------------------------------------------------
    TargetError = 1e-5
    Error = 1
    Alpa = 0.7
    Iter = 0
    momentum = 1
    E = 1;

    t = np.zeros((len(isi_teks_desimal),1))

    # print(int(isi_teks_desimal[1])/2)
    for i in range(len(isi_teks_desimal)):
        t[i] = int(isi_teks_desimal[i]) / 122
    #------------------------------------------------------------------------------

    # print(t)
    #PELATIHAN
    #------------------------------------------------------------------------------
    # h=np.matrix([])
    h = np.zeros(nHiddenLayer1)
    dV = np.zeros(nHiddenLayer1*len(isi_teks))
    dV = np.reshape(dV,(len(isi_teks),nHiddenLayer1))

    simpanV ='' #np.zeros(np.size(V))



    dEy = np.zeros(len(isi_teks_desimal))
    dEy = np.reshape(dEy,(len(isi_teks),1))

    y = np.zeros(len(isi_teks_desimal))

    deltaW = np.zeros(nHiddenLayer1*len(isi_teks))
    deltaW = np.reshape(deltaW,(nHiddenLayer1,len(isi_teks)))

    c= []
    cc = 0
    while E>TargetError:
    # while Iter<1:
        Iter = Iter +1
        for n in range(1):
            # print(W)
            #HIDDEN LAYER 1
            #-----------------------------------------------------------------------
            c = W*N_isi_teks+B1
            for i in range(nHiddenLayer1):
                h[i]= ((2/(1+np.exp((-2*-c[i])))))
            h = np.reshape(h,(nHiddenLayer1,1))
            #-----------------------------------------------------------------------

            #HIDDEN LAYER 2
            #----------------------------------------------------------------------

            yy = V*h+B2
            for i in range(len(isi_teks)):
                y[i]= ((2/(1+np.exp((-2*-y[i])))))
            y = yy
            #----------------------------------------------------------------------

            #---------------------------------------------------------------------

              ##########################
             ###------BACKWARD------###
            ##########################


            #ERROR NET
            #-----------------------------------------------------------------------


            e = -(np.matrix(y) - np.matrix(t))

            for i in range(len(isi_teks)):
                dEy[i] = e[i] * y[i] * (1-y[i])


            dH = np.transpose(V)*dEy


            for i in range(len(isi_teks)): #untuk baris
                for j in range(nHiddenLayer1):
                    dV[i,j] = dEy[i] * h[j]

            # print(W)
            for i in range(nHiddenLayer1): #untuk baris
                for j in range(len(isi_teks)):
                    deltaW[i,j] = dH[i] * N_isi_teks[j]

            #UPDATE PEMBOBOT
            #----------------------------------------------------------------------
            W  = (momentum * W)+(deltaW * Alpa)

            B1 = momentum * B1 + dH * Alpa


            V  = momentum * V  +  dV * Alpa

            B2 = momentum * B2 + dEy * Alpa

            #-----------------------------------------------------------------------

        E=np.sum(0.5 * (np.power(e,2)))
        #print(h)
        #print(y)
        print('ITERASI ke -',Iter,' || Error =',E)
    #----------------------------------------------------------------------- --------

    ################################################################################
    #---------------PROSES KOMPRESI DENGAN VARIABEL HIDDEN LAYER-------------------#
    ################################################################################
    c = W*N_isi_teks+B1
    for i in range(nHiddenLayer1):
        h[i]= ((2/(1+np.exp((-2*-c[i])))))
    h = np.reshape(h,(nHiddenLayer1,1))

    # print(h)

    #-------------------------------------------------------------------------------
    #menyimpan pembobot v
    file_v = open("pembobot/pembobotV.txt","w")
    # print(np.size(V,1))

    iterasiK=0;
    iterasiB=0;
    for i in range(np.size(V)):

        if np.mod(i,np.size(V,1))==0:
            iterasiK=0
            iterasiB=iterasiB+1

        # simpanV.append(" ",V[iterasiB-1,iterasiK])
        simpanV = simpanV+"{0} ".format(V[iterasiB-1,iterasiK])
        # print(V[iterasiB-1,iterasiK])
        # isi_teks_desimal.append(str(ord(isi_teks[i])))

        # print("K= ",iterasiK,"| B = ",iterasiB-1,"| i= ",i)
        iterasiK=iterasiK+1
    # A=[0.001 0.002]



    file_v.write(str(simpanV))
    file_v.close()

    #menyimpan ukuran W
    #print(V)
    file_v = open("pembobot/sizeV.txt","w")
    ukuran = "{0} {1}".format(np.size(V,0),np.size(V,1))
    file_v.write(ukuran)
    file_v.close()


    #menyimpan pembobot b
    ################################################################################
    file_v = open("pembobot/pembobotB.txt","w")
    # print(np.size(V,1))

    iterasiK=0;
    iterasiB=0;
    simpanB2=''
    for i in range(np.size(B2)):

        if np.mod(i,np.size(B2,1))==0:
            iterasiK=0
            iterasiB=iterasiB+1

        # simpanV.append(" ",V[iterasiB-1,iterasiK])
        simpanB2 = simpanB2+"{0} ".format(B2[iterasiB-1,iterasiK])
        # print(V[iterasiB-1,iterasiK])
        # isi_teks_desimal.append(str(ord(isi_teks[i])))

        # print("K= ",iterasiK,"| B = ",iterasiB-1,"| i= ",i)
        iterasiK=iterasiK+1
    # A=[0.001 0.002]



    file_v.write(str(simpanB2))
    file_v.close()


    #menyimpan ukuran W
    ukuran=''
    file_v = open("pembobot/sizeB2.txt","w")
    ukuran = "{0} {1}".format(np.size(B2,0),np.size(B2,1))
    file_v.write(ukuran)
    file_v.close()


    ################################################################################
    # hasil_normalisasi = np.zeros((nHiddenLayer1,1))
    #
    # maksimal_hasil_normalisasi = np.max(h)
    # minimal_hasil_normalisasi = np.min(h)
    # for i in range(nHiddenLayer1):
    #     hasil_normalisasi[i]=np.round((h[i] - minimal_hasil_normalisasi) / (maksimal_hasil_normalisasi-minimal_hasil_normalisasi)*190)


    #simapn maks and min
    maksimal_hasil_normalisasi = np.max(h)
    minimal_hasil_normalisasi = np.min(h)

    minmaks = '{0} {1}'.format(maksimal_hasil_normalisasi,minimal_hasil_normalisasi)
    file_v = open("pembobot/minmaks.txt","w")
    file_v.write(minmaks)
    file_v.close()
    #uvah ke char

    teks_hasil_kompresi=''
    for i in range(nHiddenLayer1):
        teks_hasil_kompresi=teks_hasil_kompresi+'{0}'.format(chr((np.round((h[i] - minimal_hasil_normalisasi) / (maksimal_hasil_normalisasi-minimal_hasil_normalisasi)*113))+14))

    #menyimpan hasil kompresi
    file_v = open("hasilkompresi.txt","w")
    file_v.write(teks_hasil_kompresi)
    file_v.close()

    #print('Hasil kompresi')
    #print(h)


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       SUCCESS          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="                                          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="_______________________________________________",fg="red",bd=10,anchor='w',bg="powder blue")


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       Hasil Kompresi          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',8,'bold'),text=teks_hasil_kompresi,fg="red",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=9,columnspan=10)




#-------------------------------------------------------------------------------------------
def btnDekompres():
    lblInfo = Label(Tops, font=('arial',30,'bold'),text=".....PLEASE WAIT...",fg="Steel Blue",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    files = open(root.fileName,'r')
    hasil = files.read()
    kata = []

    iter1=0
    for i in range(len(hasil)):
        iter1=iter1+1
        kata.append(ord(hasil[i]))


    dV= np.zeros(iter1)
    h = np.reshape(dV,(iter1,1))


    files = open('pembobot/minmaks.txt','r')
    minmaks = files.read()
    minmaks1 = minmaks.split(' ')
    #ambil maksimal
    maksimal_hasil_normalisasi = float(minmaks1[0])

    #ambil minimal
    minimal_hasil_normalisasi = float(minmaks1[1])
    files.close()

    for i in range(iter1):
        #print(i,'|iterasi|',iter1)
        h[i]=((((maksimal_hasil_normalisasi - minimal_hasil_normalisasi)/113)*kata[i])+minimal_hasil_normalisasi)

    # print(h)
    h=np.matrix(h)
    #print(np.size(h),'||',np.size(kata))

    #membuka file pembobot V
    #-------------------------------------------------------------------------------
    files = open('pembobot/pembobotV.txt','r')
    kalimat = files.read()
    kata = kalimat.split(' ')

    for i in range(len(kata)-1):
        kata[i]=float(kata[i])

    files = open('pembobot/sizeV.txt','r')
    sizeV = files.read()
    sizeV = sizeV.split(' ')

    dV = np.zeros(int(sizeV[0])*int(sizeV[1]))
    V = np.reshape(dV,(int(sizeV[0]),int(sizeV[1])))

    iterasiK=0
    iterasiB=0
    for i in range(len(kata)-1):
        V[iterasiB,iterasiK]=kata[i]
        iterasiK=iterasiK+1

        if np.mod(iterasiK,int(sizeV[1]))==0:
            iterasiK=0
            iterasiB=iterasiB+1

    V=np.matrix(V)

    #membuka file pembobot B
    #-------------------------------------------------------------------------------
    files = open('pembobot/pembobotB.txt','r')
    kalimatB = files.read()
    kata = kalimatB.split(' ')

    for i in range(len(kata)-1):
        kata[i]=float(kata[i])

    files = open('pembobot/sizeB2.txt','r')
    sizeB2 = files.read()
    sizeB2 = sizeB2.split(' ')

    dB2 = np.zeros(int(sizeB2[0])*int(sizeB2[1]))
    B2 = np.reshape(dB2,(int(sizeB2[0]),int(sizeB2[1])))

    iterasiK=0
    iterasiB=0
    for i in range(len(kata)-1):
        B2[iterasiB,iterasiK]=kata[i]
        iterasiK=iterasiK+1

        if np.mod(iterasiK,int(sizeB2[1]))==0:
            iterasiK=0
            iterasiB=iterasiB+1

    B2=np.matrix(B2)


    #PROSES dekompresi
    #===========
    y = np.zeros(int(sizeB2[0]))
    #print(np.size(V),'||',np.size(V))
    yy = V*h+B2
    for i in range(int(sizeB2[0])):
        y[i]= ((2/(1+np.exp((-2*-y[i])))))
    y = yy


    #-----------
    hasil_akhir = y * 122
    # hasil_akhir = np.round(hasil_akhir,2)
    # print(hasil_akhir)

    ##KONVERSI
    hasil_kata=""
    for i in range(len(hasil_akhir)):
        xyz=hasil_akhir[i]-np.round(hasil_akhir[i],0)

        if xyz>=0.5:
            hasil_akhir[i]=hasil_akhir[i]
        else:
            if (xyz-0.4)>=0.05:
                hasil_akhir[i] = hasil_akhir[i]+0.1
            else:
                hasil_akhir[i]=hasil_akhir[i]

    ##KONVERSI
    hasil_kata=""
    for i in range(len(hasil_akhir)):
        # print(chr(np.round(hasil_akhir[i]))," || ",hasil_akhir[i])
        hasil_kata = hasil_kata + chr(np.round(hasil_akhir[i]))


    file_v = open("hasilDekompresi.txt","w")
    file_v.write(hasil_kata)
    file_v.close()





    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       SUCCESS          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=7,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="                                          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',30,'bold'),text="_______________________________________________",fg="red",bd=10,anchor='w',bg="powder blue")


    lblInfo = Label(Tops, font=('arial',30,'bold'),text="       Hasil Dekompresi          ",fg="Green",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=8,columnspan=10)

    lblInfo = Label(Tops, font=('arial',8,'bold'),text=hasil_kata,fg="red",bd=10,anchor='w',bg="powder blue")
    lblInfo.grid(row=9,columnspan=10)




root.mainloop()
>>>>>>> 768066e542dfd3e1719ef09bcbb88526976b49f4
