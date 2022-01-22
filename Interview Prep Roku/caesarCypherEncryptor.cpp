#include <iostream>

#include <string>
using namespace std;




string caesarCypherEncryptor(string str, int key) {
  // Write your code here.
	string newString = str;

	int newkey = key %26;

	for (int i = 0; i < str.length(); i++){
		int newletter = newkey + int(str[i]);
		
		if (newletter <= 122){
			newString[i] = newletter;
		}
		else{
			newString[i] = newletter%122 + 96;
		}

		// cout<<str[i]<<endl;
	}
		// cout << str.length() << "ss" << endl;
	// cout << newString.length() << "ss" << endl;
  return newString;
}


int main()
{
   string str1 = caesarCypherEncryptor("xyz", 2);

   cout << str1 << endl;

   return 0;
 }