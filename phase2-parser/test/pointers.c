int main(void){
    int a=6,b=2;
    int c   = a * b;      
    int *p  = &a;        
    int d   = *p;         
    int **pp= &p;         
    int e   = **pp;       
    a *= b;               
    *p = *p * *p;         
    int f = a**p;        
    printf("%d", c+d+e+f);
    return 0;
}
