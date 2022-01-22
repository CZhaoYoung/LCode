#include <iostream>
#include <iterator>
#include <map>
using namespace std;

int main(int argc, char const *argv[]){
	
	map<int, int> g;

	g.insert(pair<int, int>(1,30));
	g.insert(pair<int, int>(2,20));
	g.insert(pair<int, int>(3,40));
	g.insert(pair<int, int>(4,50));
	g.insert(pair<int, int>(4,80));
	g.insert(pair<int, int>(6,10));
	g.insert(pair<int, int>(7,20));
	g.insert(pair<int, int>(8,90));
	g.insert(pair<int, int>(9,60));


	// print
	map<int, int>::iterator itr;
	cout << "\n The map q is: \n";
	cout << "\tKey\tElement\n";

	for(itr = g.begin(); itr != g.end(); ++itr){
		cout << "\t" << itr->first << "\t" << itr->second << "\n";
	}
	cout << endl;

	// assign 
	map<int, int> g2 (g.begin(), g.end());

	cout << "\nThe map g2 after assign from g is: \n";
	for(itr = g2.begin(); itr != g2.end(); ++itr){
		cout << "\t" << itr->first << "\t" << itr -> second << "\n";
	}
	cout << endl;

	// remove all elements with key = 4;

	int num; 
	num = g2.erase(4);
	cout << "\ng2.erase(4): " << num << " removed \n" ;

	cout << "\tKey\tElement\n";
	for(itr = g2.begin(); itr != g2.end(); ++itr){
		cout << "\t" << itr->first << "\t" << itr -> second << "\n";
	}

	return 0;
}