int main(void){
    int a=6,b=2,c=0;
    c = a+b; c = a-b; c = a*b; c = a/b; c = a%b;
    c = a++; c = a--; c = ++a; c = --a;
    a+=b; a-=b; a*=b; a/=b; a%=b;
    c = (a==b); c = (a!=b); c = (a<b); c = (a>b); c = (a<=b); c = (a>=b);
    c = (a&&b); c = (a||b); c = (!a);
    c = a&b; c = a|b; c = a^b; c = ~a; c = a<<b; c = a>>b;
    a<<=b; a>>=b; a&=b; a|=b; a^=b;
    
    c = a+++++b;   
                      
    c = a---b;    
    c = a-->b;     
    c = a<<-b;     
    c = a<-b;      
    c = a&&&b;     
    printf("%d", &c);
    return 0;
}
