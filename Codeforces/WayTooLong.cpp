#include <iostream>
#include <cstring>
using namespace std;
 
int main() {
	string s;
	cin>>s;
	int countupper=0,countlower=0;
	for(int i=0;i<s.size();i++){
	    if(isupper(s[i])){
	        countupper++;
	    }else{
	        countlower++;
	    }
	}
	if(countlower<countupper){
	    char answer;
	    for(int i=0;i<s.size();i++){
	        answer=toupper(s[i]);
	        cout<<answer;
	    }
	}else{
	    char answer;
	    for(int i=0;i<s.size();i++){
	        answer=tolower(s[i]);
	        cout<<answer;
	    }
	}
	return 0;
}