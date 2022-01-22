// https://www.geeksforgeeks.org/vector-in-cpp-stl/

#include <iostream>
#include <vector>

using namespace std;
int main()
{
    vector<int> g1;
    // ==========
    // Iterators
    // ==========
  
    // for (int i = 1; i <= 5; i++)
    //     g1.push_back(i);
  
    // cout << "Output of begin and end: ";
    // for (auto i = g1.begin(); i != g1.end(); ++i)
    //     cout << *i << " ";
  
    // cout << "\nOutput of cbegin and cend: "; // Returns a constant iterator 
    // for (auto i = g1.cbegin(); i != g1.cend(); ++i)
    //     cout << *i << " ";
  
    // cout << "\nOutput of rbegin and rend: "; // Returns a reverse iterator
    // for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir)
    //     cout << *ir << " ";
  
    // cout << "\nOutput of crbegin and crend : "; // Returns a constant&reverse iterator
    // for (auto ir = g1.crbegin(); ir != g1.crend(); ++ir)
    //     cout << *ir << " ";
  	

    // ==========
    // Capacity
    //===========
 //    cout << endl;

 //    for (int i = 1; i <= 5; i++)
 //    	g1.push_back(i);

 //    cout << "Size: " << g1.size() << endl; //length
 //    cout << "Capacity: " << g1.capacity() << endl; //R eturns the size of the storage space currently allocated to the vector expressed as number of elements
 //    cout << "Max_Size: " << g1.max_size() << endl;

 //    // resize
 //    g1.resize(4);
 //    cout << "Resized: " << g1.size() << endl;

 //    // check if empty
 //    if(g1.empty()==false){
 //    	cout << "Vector is not empty" << endl;
 //    }
 //    else{
 //    	cout << "Vector is empty" << endl;
 //    }

 //    for (auto i = g1.begin(); i != g1.end(); ++i){
	// cout << *i << " ";
	// }
	// cout << endl;

 //    // shrink
 //    g1.shrink_to_fit(); // Reduces the capacity of the container to fit its size and destroys all elements beyond the capacity.
 //    cout << "Vector elements are: ";

 //    for (auto i = g1.begin(); i != g1.end(); ++i){
 //    	cout << *i << " ";
 //    }
 //    cout << endl;

    // ==========
    // Element access
    // =============

	// for (int i = 0; i < 10; ++i){
	// 	g1.push_back(i*10);
	// }

	// for (auto i = g1.begin(); i != g1.end(); ++i){
	// 	cout << *i << " ";
	// }
	// cout << endl;
	
	// // These two are the same. 
	// // Return the reference to the element at position [] in the vector
 //    cout << g1[0] << endl;
 //    cout << "at : g1.at(4) = " << g1.at(4) << endl;

 //    cout << g1.front() << endl;
 //    cout << g1.back() << endl;

    // ==========
    // Modifiers
    // ==========
	
	// fill the array with 10 five times 
    vector <int> v;
    v.assign(5, 10);

    cout << "The vector elements are:" ;
    for (int i = 0; i < v.size(); i++){
    	cout << v[i] << " ";
    }
    cout << endl;

    // insert 
    v.push_back(15);
    int n = v.size();
    cout << "The last element of v: " << v[n-1];

    // removes the last
    v.pop_back();

    // inserts 5 at the beginning
    v.insert(v.begin(), 5);

    cout << "\nThe first element is: " << v[0];
  
    // removes the first element
    v.erase(v.begin());
  
    cout << "\nThe first element is: " << v[0];
  
    // inserts at the beginning
    v.emplace(v.begin(), 5);
    cout << "\nThe first element is: " << v[0];
  
    // Inserts 20 at the end
    v.emplace_back(20);
    n = v.size();
    cout << "\nThe last element is: " << v[n - 1];
  
    // erases the vector
    v.clear();
    cout << "\nVector size after erase(): " << v.size();


    return 0;
}