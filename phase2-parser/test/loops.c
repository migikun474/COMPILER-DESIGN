int main(void){
    int i, s, n=3;

    for(s=0,i=0;i<n;i++) s+=i;            printf("for sum 0..2      = %d\n", s);
    i=0; s=0; while(0) s++;               printf("while(0) body ran = %d times\n", s);
    i=0; s=0; do s++; while(0);           printf("do-while(0) ran   = %d time\n", s);
    return 0;
}
