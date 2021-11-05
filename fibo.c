#include<stdio.h>

int main(){
int n;
int a=0,b=1;

scanf("%d",&n);
printf("0\n");
printf("1\n");
fib(n,a,b);

return 0;

}

void fib(int n,int a,int b){
    int c;
    if(n>1){
        c=a+b;
        a=b;
        b=c;
        printf("%d\n",c);
        fib(n-1,a,b);
    }

}