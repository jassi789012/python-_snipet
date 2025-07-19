#include<iostream>
using namespace std;

int main(){
    int a= 3;
    int* b=&a;
    cout<<"Adress assigned in b:\t"<<b<<endl;
    cout<<"Value of variale assigned in b:\t"<<*b<<endl;
    return 0;
}