#include <iostream>
#include <iterator>
#include <list>

using namespace std;

void showlist(list<int> g){

	list<int> :: iterator it;
	for(it = g.begin(); it != g.end(); ++it){
		cout << ' ' << *it;
	}
	cout << endl;
}

int main(int argc, char const *argv[])
{
	list<int> gglist1, gglist2;

	for(int i = 0; i < 10; ++i){
		gglist1.push_back(i * 2);
		gglist2.push_back(i * 3);
	}

    cout << "\nList 1 (gglist1) is : ";
    showlist(gglist1);
 
    cout << "\nList 2 (gglist2) is : ";
    showlist(gglist2);


	cout<< "\ngglist1.front(): " << gglist1.front();
	cout << "\ngglist1.back(): " << gglist1.back();

	cout << "\ngglist1.pop_front(): ";
	gglist1.pop_front();
	showlist(gglist1);

	cout << "\ngglist2.pop_back(): ";
	gglist2.pop_back();
	showlist(gglist2);

	cout <<"\n gglist1.reverse(): ";
	gglist1.reverse();
	showlist(gglist1);	

	cout << "\n gglist2.sort(): ";
	gglist2.sort();
	showlist(gglist2);


	return 0;
}