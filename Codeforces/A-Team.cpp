#include <iostream>
using namespace std;
int main(){
    
    int n;
    cin>>n;
    int counterTotal=0;
    while(n--){
        int counter=0;
        
        int scores[3];
        for(int i=0;i<3;i++){
            cin>>scores[i];
        }
        for(int i=0;i<3;i++){
            if(scores[i]==1){
                counter+=1;
            }
        }
        if(counter>1){
            counterTotal+=1;
        }
        
    }
    cout<<counterTotal;
 
 
 
}