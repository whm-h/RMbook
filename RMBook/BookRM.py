import random
import os

class RM:
    def Unlock(name):
        list1 = []
        list2 = []
        with open(f'{name}','r') as f1:
            a = f1.read()
            lena = len(a)
            la = 0
            for item in range(lena):
                b = a[la]
                list1.append(b)
                la += 1

        with open(f'{name}.key','r') as f1:
            a = f1.read()
            lena = len(a)
            la = 0
            for item in range(lena):
                b = a[la]
                list2.append(b)
                la += 1

        HM = 0
        listf = []
        lena = lena * 2
        try:
            for item in range(lena):
                lc1 = list1[HM]
                lc2 = list2[HM]
                if lc1 == lc2:
                    HM += 1
                else:
                    listf.append(lc1)
                    list1.remove(list1[HM])

            with open(f'Unlock_{name}.txt','a') as f:
                f.writelines('\n')
                f.writelines(listf)
        except:
            with open(f'Unlock_{name}.txt','a') as f:
                f.writelines('\n')
                f.writelines(listf)
    def Lock(text,name = 'lock', protocol = 'S3'):
        try:
            os.remove(f"{name}.key")
        except:
            open(f"{name}.key", "a")
    
        AH = 0
        CC = len(text)
        lia = []
        for item in range(CC):
            QV = (text[AH])
            lia.extend(QV)
            AH += 1
        lia.append('1')
        QM = 0
        lia2 = lia.copy()
        QH = len(lia)
        for item in range(QH):
            AK = (lia[QM])
            with open(f"./Sfiles/{secore}", "r") as file:
                allText = file.read()
            words = list(map(str, allText.split()))
            AK = random.choice(words)
            AK = str(AK)
            AK = AK + '1'
            with open(f"{name}.key", "a") as file1:
                file1.writelines(AK)
            SD = lia.extend(AK)
            QL = (lia[0])
            lia.remove(QL)
            AQ = (lia2[QM])
            lia.extend(AQ)
            QM += 1
        lia.append('1')
        with open(f'{name}','w') as f:
            f.writelines(lia)
        AS = 0
        lia3 = lia.copy()
