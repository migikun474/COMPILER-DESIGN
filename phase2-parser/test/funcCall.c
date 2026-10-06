
int foo(int a,int b,int c,int d){
  return -a+b-c*d/a;
}

int main(){
  int a=10,b=20,*c,d=30;
  c = &d;
  b = foo(a--,--a,a+b,a+*c);
    printf("%d\n",b%d);
}
