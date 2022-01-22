#include <iostream>

#include <string>

#include <vector>

#include <iostream>

#include <unordered_map>

#include <algorithm>

using namespace std;

// vector<string> returnString(){

// 	vector<string> v  {"+4", "-3", "+3", "-11"};

// 	return v;

// }

// int main(){

// 	char greeting[6] = {'H', 'E', 'T'};

// 	std::vector<std::string> v  {"+4", "-3", "+3", "-11"};

// 	cout << v[1][1] << endl;

// 	vector<string> res = returnString();

// 	for (auto i: res){
// 		cout << i << ' ';
// 	}

// 	cout << endl;
	
// 	for (std::vector<string>::const_iterator i = res.begin(); i != res.end(); ++i)
//     	std::cout << *i << ' ';
	
// 	cout << endl;
// }

int main(int argc, char const *argv[]){

	vector<string> words = {"yo", "oy", "teet", "test", "ou", "uo"};

	unordered_map<string, vector<string>> anagrams;
	
	for(auto word : words){
		string sortedWord = word;
		
		sort(sortedWord.begin(), sortedWord.end());
		
		if(anagrams.find(sortedWord) != anagrams.end()){
			anagrams[sortedWord].push_back(word);
		}
		else{
			anagrams[sortedWord] = vector<string>{word};
		}
	}
	
	vector<vector<string>> output={};
	
	// unordered_map<string, vector<string>>::iterator itr;

	// for(itr = anagrams.begin(); itr != anagrams.end(); ++itr){
	// 	cout << '\t' << itr->first << '\t' << itr->second << endl;
	// }

	for(auto v: anagrams){
		output.push_back(v.second);	

		cout << endl;
		
	}
	

	return 0;
}