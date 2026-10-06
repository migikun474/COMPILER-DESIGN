
int main(void){
    int x=0; char buf[32];
    printf("%d\n", 1);
    printf("%s %c %5.2f %%\n", "s", 'c', 1.5);   
    printf("tab\there\nnewline\n");
    printf("brace { and } and /* and */ and \" \n");  
    printf("");                                  
    scanf("%d", &x);
    scanf("%31s", buf);
    printf("%d %s\n", x, buf);
    return 0;
}
