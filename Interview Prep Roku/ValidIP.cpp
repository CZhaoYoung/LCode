#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

bool isValid(string str);
string join(vector<string> strings);


vector<string> validIPAddresses(string str) {
  // Write your code here.
	vector<string> ipAddressFound;
	
	for (int i = 1; i < min((int)str.length(), 4); i++){
		vector<string> currentIPAddressParts = {"", "", "", ""};
		currentIPAddressParts[0] = str.substr(0, i);
		
		if (!isValid(currentIPAddressParts[0])){
			continue;
		}
		
		for (int j = i+1; j< i+ min((int)str.length() - i, 4); j++){
			currentIPAddressParts[1] = str.substr(i, j-i);
			if (!isValid(currentIPAddressParts[1])){
				continue;
			}
			
			for (int k = j+1; k < j+ min((int)str.length() - j, 4); k++){
				currentIPAddressParts[2] = str.substr(j, k-j);
				currentIPAddressParts[3] = str.substr(k);
				
				if(isValid(currentIPAddressParts[2]) && isValid(currentIPAddressParts[3])){
					ipAddressFound.push_back(join(currentIPAddressParts));
				}
			}
		}
	}
  return ipAddressFound;
}

bool isValid(string str){
	int stringAsInt = stoi(str);
	
	if(stringAsInt > 255){
		return false;
	}
	return str.length() == to_string(stringAsInt).length(); // check for leading 0;
}

string join(vector<string> strings){
	string s;
	for(int m = 0; m < strings.size(); m++){
		s += strings[m];
		if(m < strings.size() - 1){
			s += ".";
		}
	}
	return s;
}


int main(int argc, char const *argv[])
{
	
	vector<string> Ip = validIPAddresses("123123123123");


	for (auto i = Ip.begin(); i != Ip.end(); ++i){
		cout << *i << " ";
	}
	cout << endl;

	return 0;
}
