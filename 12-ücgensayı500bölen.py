def ucgensayi(n=2000):

    while True:
        sonuc = (n * (n + 1)) / 2
        i=1
        bolunensayisi=0
        while i<=sonuc:
            if(sonuc%i==0):
                bolunensayisi+=1
                i+=1
            else:
                i+=1
        n+=1
        print(n, sonuc, i, bolunensayisi)
        if(bolunensayisi>=288):
            print(sonuc)
            break
ucgensayi()