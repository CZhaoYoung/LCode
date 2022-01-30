#include <iostream>
using namespace std;
// construct

// class construct {
//     int a, b;
//     construct(){
//         a = 10;
//         b = 10;
//     }
// };

// int main(){
//     construct c;
//     cout << c.a << endl;

//     cout << c.b;

//     return 0;
// }

class Shape{
    protected:
        int w, h;
    public:
        Shape(int a=0, int b=0){
            w = a;
            h = b;
        }
        int area(){
            cout << "Parent class area : " << endl;
            return 0
        }
};

class Rec : public Shape{
    public:
        Rec(int a=0; int b=0) : Shape(a, b){ }
        int area(){
            cout << "Rec area: " << endl;
            return (w*h);
        }
};

class Tri : public Shape{
    public:
        Rec(int a=0; int b=0) : Shape(a, b){ }
        int area(){
            cout << "Tri area: " << endl;
            return (w*h / 2);
        }
};

int main(){
    Shape *shape;
    Rec rec(10,7);
    Tri tri(10,5);

    shape &rec;
    shape -> area();

    shape &tri;
    shape -> area();

    return 0;
}
