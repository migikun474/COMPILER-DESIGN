int main(void){
    int  a[5] = {1,2,3,4,5};
    int  z[5] = {1};                 
    char b[4] = {'a','b','c','\0'};
    char c[]  = "abc";               
    char d    = 'a';
    int  e    = 'ab';               
    char g[]  = "a\"b\\c";
    char h[]  = "a/*not a comment*/b // nor this";
    char i[]  = "adj" "acent";       
    int j;

    printf("a       = "); for(j=0;j<5;j++) printf("%d ", a[j]); printf("\n");
    printf("z       = "); for(j=0;j<5;j++) printf("%d ", z[j]); printf("\n");
    return 0;
}
