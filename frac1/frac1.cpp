
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

int d;
vector <int > listn;
vector <int > listm;
vector <string> final_list;
//listn.reserve(160);
//listm.reserve(160);


vector<int> primeFactors(int n)
{
    vector <int> listofprimefactors;
    listofprimefactors.resize(0);
    // Print the number of 2s that divide n
    while (n % 2 == 0)
    {
        listofprimefactors.push_back(2);
        n = n/2;
    }
 
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            listofprimefactors.push_back(i);
;
            n = n/i;
        }
    }
 
    if (n > 2)
        listofprimefactors.push_back(n);
    // for(int i=0; i < listofprimefactors.size(); i++){
    //     cout << listofprimefactors.at(i) << ' ';
    // }

    return (listofprimefactors);

}     
 
bool comparetwo(vector <int> list1, vector <int>list2){
    for (int i = 0; i < list1.size(); i++){
        for (int j = 0; j < list2.size(); j++) {
            if (list1[i] == list2[j]){
                return false;
                
            }


        }
    }
    return true;
}

void print_vector(string title, vector<int> vec){
            cout << title << ": ";
            for(int x: vec){
                cout << x << ", ";
            }
            cout << endl;
}

int main (){
    ifstream inFile;
    ofstream outFile;
    const string filepath = "frac1.in";
    inFile.open(filepath);
    inFile >> d;
    

    vector<int> listholder = primeFactors(1);
    for(int x : listholder){
        cout << " " << x;
    }
    for (int i = 1; i < d-1; i++){
        for (int j = i+1; j < d; j++) {
            vector <int> listholder = primeFactors (i);
            vector <int> listholder2 = primeFactors (j);
            cout << i << "  " << j << endl;
            print_vector("listholder", listholder);
            print_vector("listholder2", listholder2);
            if ( listholder2.size() > 0 && comparetwo (listholder,listholder2)){
                cout << "found one" << endl;
                string str1 = to_string(i);
                string str2 = to_string(j);
                string str3 = str1+'/'+str2;
                final_list.push_back(str3);
            }
        }
     }
    for(int i=0; i < final_list.size(); i++){
       cout << final_list.at(i) << ' ';
    }
}
