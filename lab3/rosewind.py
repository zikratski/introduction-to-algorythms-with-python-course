import sys, random, math, matplotlib.pyplot as plt
def countdir(line,wdir):
        sdir = ''
        countcomma = 0
        for i in line:
                if i == ',':
                        countcomma +=1
                if countcomma == 5:
                        sdir += i
                # print(sdir)
        # print(sdir)
        sdir = float(sdir[1:])-22.5
        # print(sdir)
        lambd = int(sdir // 45)
        #print(sdir,lambd)
        wdir[lambd] += 1

if __name__ == '__main__':
        fil = sys.argv[1]
        #fil = 'minsk2022.csv'
        wdir = [0 for i in range(8)]
        with open(fil, 'r') as f:
                for line in f:
                        if 'wdir' in line:
                                continue
                        countdir(line,wdir)
                wdir = [wdir[-1]]+[wdir[i] for i in range(len(wdir)-1)]
        # print(wdir)
        rad_ar = [math.pi/2,math.pi/4,0,7*math.pi/4,3*math.pi/2,5*math.pi/4,math.pi,3*math.pi/4]
        x_ar = [round(wdir[i]*math.cos(rad_ar[i]),4) for i in range(8)]
        y_ar = [round(wdir[i]*math.sin(rad_ar[i]),4) for i in range(8)]
        x_ar.append(x_ar[0])
        y_ar.append(y_ar[0])
        textdir = ['N','NE','E','SE','S','SW','W','NW']

        plt.figure()
        plt.title('Роза ветров Минска')
        plt.plot(x_ar,y_ar,'b-',lw=1.5)
        plt.grid(visible=True,which='major')
        plt.xlim([min(x_ar)-5,max(x_ar)+5])
        plt.ylim([min(y_ar)-5,max(y_ar)+5])
        for i in range(8):
                plt.text(x_ar[i]+1,y_ar[i]+1,textdir[i])
                plt.arrow(0,0,x_ar[i],y_ar[i],width=0.0001,head_width=1.9)
        plt.show()
