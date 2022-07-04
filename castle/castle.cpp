/**
ID: jessety1
LANG: C++
TASK: castle
*/

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;


const int MAX_M = 50;
int castle [MAX_M][MAX_M];
bool castle_visited [MAX_M][MAX_M];
int n; //number of columns
int m; //number of rows;

int room_count = 0;
int largest_room = 0;
int room_size = 0;

int combine_room_size = 0;

struct Room{
        int r;
        int c;
        char d;
};

struct RMIndex{
    int rm1;
    int rm2;
    int total_length;
};

vector < vector<Room> > room_list;
vector <RMIndex> comb_list;

bool compareRoom(const Room &ra, const Room &rb){
    if (ra.c > rb.c){
        return false;
    }
    else if(ra.c < rb.c){
        return true;
    }
    else{
        return (ra.r > rb.r);
    }
}

bool compareRMIndex(const RMIndex &ra, const RMIndex &rb){
    return ra.total_length > rb.total_length;
}

void connect (int r, int c, vector<Room> & connectroom) {
    int rn = castle[r][c];
    if (castle_visited[r][c]){
        return;
    }

    castle_visited[r][c] = true;
    room_size += 1;
    // cout << "-> room " << r << "  "  << c << endl;
    Room x;
    x.r = r;
    x.c = c;
    x.d = 'X';
    // cout << "->>> x room " << x.r << "  "  << x.c << endl;
    connectroom.push_back(x);
    // cout << "-> connnection room size " << connectroom.size() << endl;
    if (room_size > largest_room){
        largest_room = room_size;
    //print(f"room[{r}][{c}]: {rn}")
    }
    if ((rn & 1) == 0){
        connect(r,c-1,connectroom);
    }
    if ((rn & 2) == 0){
        connect(r-1,c,connectroom);
    }
    if ((rn & 4) == 0){
        connect(r,c+1,connectroom);
    }
    if ((rn & 8) == 0){
        connect(r+1,c,connectroom);
    }
    // cout << "   connnection room size " << connectroom.size() << endl;
}

vector<Room> comparetworoom( vector<Room> & list1, vector<Room> & list2){

    // cout << "comparetworoom list 1 :::" << endl;
    // for (Room l1: list1){
    //     cout << "l1 (" << l1.r << ","<< l1.c << ","<<l1.d<<") ";
    // }
    // cout << endl;
    // cout << "comparetworoom list 2 :::" << endl;
    // for (Room l2: list2){
    //     cout << "l2 (" << l2.r << ","<< l2.c << ","<<l2.d<<") ";
    // }
    // cout << endl;

    vector<Room> wall_list;
    for (Room rm1: list1){
      for (Room rm2: list2){
        if (rm1.c == rm2.c){
            //cout << "find connect at r" << endl;
            if (abs(rm1.r-rm2.r) == 1){
                Room room;// = Room(0,0,'X');
                room.r = 0;
                room.c = 0;
                room.d = 'X';

                //print(f"[{r1[0]+1}, {r1[1]+1}], [{r2[0]+1}, {r2[1]+1}]")
                if (rm1.r > rm2.r){
                    room.r = rm1.r +1 ; //We added 1 here to match to the array index in question which starts from 1 not zero.
                }
                else{
                    room.r = rm2.r+1;
                }
                room.d = 'N';
                room.c = rm1.c+1;
                wall_list.push_back(room);
            }
        }
        else if(rm1.r == rm2.r){
            //cout << "find connect at c" << endl;
            if (abs(rm1.c-rm2.c) == 1){
                Room room;// = Room(0,0,'X');
                room.r = 0;
                room.c = 0;
                room.d = 'X';
                //print(f"[{r1[0]+1}, {r1[1]+1}], [{r2[0]+1}, {r2[1]+1}]")
                if (rm1.c > rm2.c){
                    room.c = rm2.c +1 ; //We added 1 here to match to the array index in question which starts from 1 not zero.
                }
                else{
                    room.c = rm1.c+1;
                }
                room.d = 'E';
                room.r = rm1.r+1;
                wall_list.push_back(room);
            }
        }
        else{
            continue;
        }
      }
      
    }
    return wall_list;
}
                

   
int main (){
    ifstream inFile;
    ofstream outFile;
    const string filepath = "castle.in";
    inFile.open(filepath);

    inFile >> n >> m;

    memset(castle_visited, false, sizeof(castle_visited));

    for (int i = 0; i < m; i++) {
        for(int j= 0; j < n; j++){
            inFile >> castle[i][j];
        }
    }

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++) {
            room_size = 0;
            // cout << "room = " << i << " " << j << endl;
            if ( castle_visited[i][j] == false){
                vector <Room > connectroom;
                connectroom.reserve(5000);
                connect(i,j, connectroom);
                room_count += 1;
                // cout << "*** connectroom size " << connectroom.size() << endl;
                
                room_list.push_back(connectroom);
                // cout << "room_list " << room_list.size() << endl;
            }
            else{
                // cout << "room " << i << "  " << j << " is visited \n";
            }
        }
    }

    // for(vector< Room> rmList : room_list){
    //     cout << "Room List: " << rmList.size() << endl;
    //     for(Room rm : rmList){
            
    //         cout << "rm: (" << rm.r << ", " << rm.c << ", " << rm.d << ") ";
    //     }
    //     cout << endl;
    // }


    int ct = 0;
    for(int i = 0; i < room_list.size(); i++){
        int ilength = room_list[i].size();
        for (int j=i+1; j< room_list.size(); j++){
            RMIndex rmidx;
            rmidx.rm1 = i;
            rmidx.rm2 = j;
            rmidx.total_length = room_list[i].size() + room_list[j].size(); 
            comb_list.push_back(rmidx);
            ct++;
        }
    }
    //cout <<"combsize: " << comb_list.size() << endl;
    // for (RMIndex rmi : comb_list){
    //     cout << "rm " << rmi.rm1 << ", " << rmi.rm2 << ", " << rmi.total_length << endl;
    // }
    vector<Room> wall_list;



    std::sort(comb_list.begin(), comb_list.end(), compareRMIndex);
    // comb_list.sort(key=lambda cbsize: cbsize[2], reverse=True)
    //cout <<"combsize2: " << comb_list.size() << endl;
    //for (RMIndex rmi : comb_list){
        //cout << "rm " << rmi.rm1 << ", " << rmi.rm2 << ", " << rmi.total_length << endl;
    //}
    for(int k = 0; k < ct; k++){
        RMIndex cb = comb_list[k];
        //cout << "cb " << cb.rm1 << ", " << cb.rm2 << ", " << cb.total_length << endl;
        wall_list = comparetworoom(room_list[cb.rm1], room_list[cb.rm2]);
        if(wall_list.size() != 0){
            //cout << "We found it " << endl;
            //print(wall_list, combine_room_size)
            combine_room_size = room_list[cb.rm1].size() + room_list[cb.rm2].size();
            break;
        }
    }

    std::sort(wall_list.begin(), wall_list.end(), compareRoom);
    // for(Room rm : wall_list){
    //     cout << "rm: " << rm.c << " " << rm.r << " " << rm.d << endl;
    // }
    // a = sorted(wall_list, key=lambda x: (x[1], -1*x[0]))
    // for (int i = 0; i < m; i++) {
    //     cout << "row " << i << "  :  ";
    //     for(int j= 0; j < n; j++){
    //        cout << "{ " << castle[i][j] << "," << castle_visited[i][j] << " } ";
    //     }
    //     cout << endl;
    // }


    outFile.open("castle.out");
    outFile << room_count << endl << largest_room << endl << combine_room_size << endl;
    outFile <<  wall_list[0].r << " " << wall_list[0].c << " " << wall_list[0].d << endl;
    outFile.close();
 }




    

/*
comb_list = [[0,0,0]]* (len(room_list) * len(room_list) //2)
ct = 0
for i in range(len(room_list)):
    ilength = len(room_list[i])
    for j in range(i+1,len(room_list)):
        comb_list[ct]= [i,j,ilength+len(room_list[j])]
        ct += 1

comb_list.sort(key=lambda cbsize: cbsize[2], reverse=True)
for k in range(ct):
    cb = comb_list[k]
    wall_list = comparetworoom(room_list[cb[0]], room_list[cb[1]])
    if(len(wall_list) != 0):
        #print(f"We found it")
        #print(wall_list, combine_room_size)
        combine_room_size = len(room_list[cb[0]]) + len(room_list[cb[1]])
        break

a = sorted(wall_list, key=lambda x: (x[1], -1*x[0]))
#print(a)
# print(Sorting(comb_list))

with open ('castle.out','w') as fout:
          
    fout.write(f"{room_count}\n{largest_room}\n{combine_room_size}\n{a[0][0]} {a[0][1]} {a[0][2]}\n")
*/