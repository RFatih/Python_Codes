#Sayısal Çözümleme Soru Çözücü
import math
import sympy as sym
choose_a_b=0
def f(x,eq):
    return math.floor(eq.subs({'x':x,'e':math.e})* 10**7 -((eq.subs({'x':x,'e':math.e})* 10**7)%10))/10**7 #fonksiyon

def F(x,eqturev):
    return math.floor(eqturev.subs({'x':x,'e':math.e})*10**7 -(eqturev.subs({'x':x,'e':math.e})*10**7%10) )/10**7


def issolvable(a,b,eq):
    print("f(",a,")=",float(f(a,eq)), " f(",b,")=",float(f(b,eq)))
    if((f(a,eq)<=0 and f(b,eq)>=0) or (f(b,eq)<=0 and f(a,eq)>=0)):
        print("Fonksiyonun a , b aralığında en az 1 kökü vardır")
    else:
        print("Verilen aralık hakkında işlem yapılamaz")
        return True
    return False
    
def bisection(a,b,tolerance):
    iterations=0
    oldb=olda=0
    denklem = input("Denklemi yazın= ")
    eq=sym.sympify(denklem)
    if(issolvable(a,b,eq)):
        return
    ans=((a*10**6+b*10**6))/(2*10**6)
    print(((11375+11500))/(2*10**4))
    while(abs(f(floor7(ans),eq))>0 and abs(a-b)>tolerance):
        print("a and b =",a,b,"x",iterations,"= ",
              floor6(ans),
              "e= ",floor6(f(ans,eq)))
        if( floor6(f(ans,eq))==abs(floor7(f(ans,eq)))):
            if(f(a,eq)==abs(f(a,eq))):
                a= floor6(ans)
            else:
                b=  floor6(ans)
        else:
            if(f(a,eq)==abs(f(a,eq))):
                b=  floor6(ans)
            else:
                a= floor6(ans)
        if(oldb ==b and olda == a):
            break
        oldb=b
        olda=a
        ans=((a*10**6+b*10**6))/(2*10**6)
        iterations+=1
    print("Answer= ",floor7(b)," = ",f((floor7((a+b)/2)),eq))
    
    
def regulaCalc(a,b,eq):
    return float(floor6( (a*(f(b,eq)) - b*(f(a,eq)) )/( f(b,eq) - f(a,eq))))

def regulaFalsi(a,b,tolerance):
    iterations=0
    denklem = input("Denklemi yazın= ")
    eq=sym.sympify(denklem)
    if(issolvable(a,b,eq)):
        return
    
    while(floor6(abs(f(abs(regulaCalc(a,b,eq)),eq)))>0):
        print("a and b =",a,b,"x",iterations,"= ",
              regulaCalc(a,b,eq),
              "e= ",floor6(f(regulaCalc(a,b,eq),eq)))
        
        if( regulaCalc(a,b,eq)==abs(regulaCalc(a,b,eq))):
            if(a==abs(a)):
                a=regulaCalc(a,b,eq)
            else:
                b=regulaCalc(a,b,eq)
        else:
            if(a==abs(a)):
                b=regulaCalc(a,b,eq)
            else:
                a=regulaCalc(a,b,eq)
        
        iterations+=1
        print("a and b =",a,b,"x",iterations,"= ",
              regulaCalc(a,b,eq),
              "e= ",floor6(f(regulaCalc(a,b,eq),eq)))
     
    print("Answer ==",regulaCalc(a,b,eq))
def floor6(a):
    return float(math.floor(a*10**6)/10**6)
def floor7(a):
    if (a*10**7 % 5 !=0):
        return floor6(a)
    return float(math.floor(a*10**8 - (a*10**8%10))/10**8)
def fixediter(a,b,tolerance):
    iterations=xi=0
    x= sym.Symbol('x')
    e=sym.Symbol('e')
    e=math.e
    denklem = input("Denklemi yazın= ")
    eq=sym.sympify(denklem)
    multiplier = 10 ** 6
    if(issolvable(a,b,eq)):
        return 
    denklem = input("X i çektiğiniz halini yazın= ")
    eqturev= sym.sympify(denklem)# burada x i çekip bulduğun fonksiyon olacak
    eqcozum=eqturev
    eqturev=sym.diff(eqturev, x)
    print(float(F(a,eqturev))," ",float(F(b,eqturev)))
    if(F(a,eqturev)>=1 or F(b,eqturev)>=1):
        print("Lutfen başka bir x çekip tekrar deneyin")
    else:
        while(abs( (math.floor(F(a,eqcozum)*multiplier)/multiplier)
                  -(math.floor(xi * multiplier) / multiplier)) >=tolerance):
            print("x",iterations,"= ",float(a),"e= ", 
                  float(math.floor((F(a,eqcozum)-xi) * multiplier) / multiplier))
            xi=math.floor(a*multiplier)/multiplier
            a= math.floor(F(a,eqcozum) * multiplier) / multiplier
            iterations+=1
def newtonC(a,eq,eq1):
    return floor6(a-(f(a,eq)/f(a,eq1)))
def newtonR(a,b,tolerance,choose_a_b):
    iterations=xi=0
    x= sym.Symbol('x')
    e=sym.Symbol('e')
    e=math.e
    denklem = input("Denklemi yazın= ")
    eq=sym.sympify(denklem)
    if (choose_a_b!= 0):
        a=choose_a_b
    else:
        if(issolvable(a,b,eq)):
            return
    eqturev1=sym.diff(eq,x)
    eqturev2=sym.diff(eqturev1,x)
    print("f = ",f(a,eq)," f'= ",f(a,eqturev1)," f''= ",f(a,eqturev2))
    
    if(f(a,eq)*f(a,eqturev2)<0):
        print("Seçilen değerle işlem yapılamıyor diğeri denenecek...")
        c=a
        a=b
        b=c
    if((f(a,eq)*f(a,eqturev2))/f(a,eqturev1)**2<1):
        xi=a
        e=1
        while(abs(e)>tolerance):
            e=floor6(xi-newtonC(xi,eq,eqturev1))
            xi=newtonC(xi,eq,eqturev1)
            print("x",iterations,"= ",xi,"e= ",e)
            iterations+=1
    
    print("Answer is ",xi)
    
    
    

def menu():
    print("********************************************************************")
    print(">>>Basit iterasyon methodu için=>>fixediter(a,b,epsilon) şeklinde fonksiyonu çağırın"
          " daha sonra önce fonksiyonu sonra x in çekilmiş halini girin")
    print("*")
    print(">>>Newton Raphson methodu için==> newtonR(a,b,epsilon,başlama noktası)"
          "şeklinde fonksiyonu çağırın.")
    print("*")
    print(">>>Regula Falsi methodu için=>> regulaFalsi(a,b,epsilon) şeklinde fonksiyonu çağırıp"
          " daha sonra kullanmak istediğiniz fonksiyonu yazınız.")
    print("*")
    
    print(">>>Bisection işlemi için=>> bisection(a,b,epsilon) şeklinde fonksiyonu çağırıp"
          " daha sonra kullanmak istediğiniz fonksiyonu yazınız.")
    
    print(">>>Epsilon değeri çok güvenilir olmasa da a ve b değerleri genellikle doğru sonuç verir"
          ". Virgülden sonraki yuvarlama hataları sonucu etkileyebilir.")
    
    print("********************************************************************")
menu()