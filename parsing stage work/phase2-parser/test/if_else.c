int main(void){
    int x=1,y=0,z=0;
    if(x) if(y) z=1; else z=2;
    if(x){ if(y) z=1; } else z=3;      
    if(x) z=1; else if(y) z=2; else z=3;
    int iffy=1, elsewhere=2, ifelse=3;
    printf("%d", z+iffy+elsewhere+ifelse);
    return 0;
}
