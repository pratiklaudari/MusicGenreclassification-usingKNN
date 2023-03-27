import csv
import math
import librosa
import numpy as nd
genre=['adhunik','bhajan','bhojpuri','classical','dohari','gazal','newa','pop','rock','selo']


def classifier(filename):
    #chroma shift

    chroma_shift_mean=float(filename[0])
    print(chroma_shift_mean)
    chroma_shift_var=float(filename[1])

    #rms

    rms_mean=float(filename[2])
    rms_var=float(filename[3])

    #sepctral centroid

    sc_mean=float(filename[4])
    sc_var=float(filename[5])

    #spectral bandwidth

    sb_mean=float(filename[6])
    sb_var=float(filename[7])

    #spectral rollof

    sr_mean=float(filename[8])
    sr_var=float(filename[9])

    #zero crossing rate

    zcr_mean=float(filename[10])
    zcr_var=float(filename[11])

    #harmonics

    harmonic_mean=float(filename[12])
    harmonic_var=float(filename[13])

    #tempo

    tempo=float(filename[14])
    #mfcc

    mfcc_mean=float(filename[15])
    mfcc_var=float(filename[16])

    #mfcc1

    mfcc1_mean=float(filename[17])
    mfcc1_var=float(filename[18])

    #mfcc2

    mfcc2_mean=float(filename[19])
    mfcc2_var=float(filename[20])
    #apply knn
    diff=[]
    file='dataset.csv'
    with open(file,'r', newline='') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        line=0
        table=0
        for row in csvreader:
            table=0
            if line==0:
                line=line+1
            elif line>=1:
                line=line+1
                for column in row:
                    if table==0:
                        table=table+1
                    elif table==1:
                        temp_csm=float(column)
                        diff1=math.pow((chroma_shift_mean-temp_csm),2)
                        diff.append(diff1)
                        table=table+1
                    elif table==2:
                        temp_csv=float(column)
                        diff2=math.pow((chroma_shift_var-temp_csv),2)
                        diff.append(diff2)
                        table=table+1
                    elif table==3:
                        temp_rmsm=float(column)
                        diff3=math.pow((rms_mean-temp_rmsm),2)
                        diff.append(diff3)
                        table=table+1
                    elif table==4:
                        temp_rmsv=float(column)
                        diff4=math.pow((rms_var-temp_rmsv),2)
                        diff.append(diff4)
                        table=table+1
                    elif table==5:
                        temp_scm=float(column)
                        diff5=math.pow((sc_mean-temp_scm),2)
                        diff.append(diff5)
                        table=table+1
                    elif table==6:
                        temp_scv=float(column)
                        diff6=math.pow((sc_var-temp_scv),2)
                        diff.append(diff6)
                        table=table+1
                    elif table==7:
                        temp_sbm=float(column)
                        diff7=math.pow((sb_mean-temp_sbm),2)
                        diff.append(diff7)
                        table=table+1
                    elif table==8:
                        temp_sbv=float(column)
                        diff8=math.pow((sb_var-temp_sbv),2)
                        diff.append(diff8)
                        table=table+1
                    elif table==9:
                        temp_srm=float(column)
                        diff9=math.pow((sr_mean-temp_srm),2)
                        diff.append(diff9)
                        table=table+1
                    elif table==10:
                        temp_srv=float(column)
                        diff10=math.pow((sr_var-temp_srv),2)
                        diff.append(diff10)
                        table=table+1
                    elif table==11:
                        temp_zcrm=float(column)
                        diff11=math.pow((zcr_mean-temp_zcrm),2)
                        diff.append(diff11)
                        table=table+1
                    elif table==12:
                        temp_zcrv=float(column)
                        diff12=math.pow((zcr_var-temp_zcrv),2)
                        diff.append(diff12)
                        table=table+1
                    elif table==13:
                        temp_hm=float(column)
                        diff13=math.pow((harmonic_mean-temp_hm),2)
                        diff.append(diff13)
                        table=table+1
                    elif table==14:
                        temp_hv=float(column)
                        diff14=math.pow((harmonic_var-temp_hv),2)
                        diff.append(diff14)
                        table=table+1
                    elif table==15:
                        temp_tm=float(column)
                        diff15=math.pow((tempo-temp_tm),2)
                        diff.append(diff15)
                        table=table+1
                    elif table==16:
                        temp_mfccm=float(column)
                        diff16=math.pow((mfcc_mean-temp_mfccm),2)
                        diff.append(diff16)
                        table=table+1
                    elif table==17:
                        temp_mfccv=float(column)
                        diff17=math.pow((mfcc_var-temp_mfccv),2)
                        diff.append(diff17)
                        table=table+1
                    elif table==18:
                        temp_mfcc1m=float(column)
                        diff18=math.pow((mfcc1_mean-temp_mfcc1m),2)
                        diff.append(diff18)
                        table=table+1
                    elif table==19:
                        temp_mfcc1v=float(column)
                        diff19=math.pow((mfcc1_var-temp_mfcc1v),2)
                        diff.append(diff19)
                        table=table+1
                    elif table==20:
                        temp_mfcc2m=float(column)
                        diff20=math.pow((mfcc2_mean-temp_mfcc2m),2)
                        diff.append(diff10)
                        table=table+1
                    elif table==21:
                        temp_mfcc2v=float(column)
                        diff21=math.pow((mfcc2_var-temp_mfcc2v),2)
                        diff.append(diff21)
                        table=table+1
    size=int(len(diff)/21)
    distance=[]
    for i in range(0,size):
        dis=0
        for j in range(0,21):
            dis=dis+diff[i*21+j]
        square=math.sqrt(dis)
        distance.append(square)
    no_of_songs_indataset=35 

    l_distance=min(distance)
    position=1
    for i in range(len(distance)):
        if distance[i]==l_distance:
            print(position)
            break
        else:
            position=position+1
    if position<=1*no_of_songs_indataset:
        return(genre[0])
    elif position<=2*no_of_songs_indataset:
        return(genre[1])
    elif position<=3*no_of_songs_indataset:
        return(genre[2])
    elif position<=4*no_of_songs_indataset:
        return(genre[3])
    elif position<=5*no_of_songs_indataset:
        return(genre[4])
    elif position<=6*no_of_songs_indataset:
        return(genre[5])
    elif position<=7*no_of_songs_indataset:
        return(genre[6])
    elif position<=8*no_of_songs_indataset:
        return(genre[7])
    elif position<=9*no_of_songs_indataset:
        return(genre[8])
    elif position<=10*no_of_songs_indataset:
        return(genre[9])
    
