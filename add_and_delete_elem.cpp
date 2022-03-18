#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;
int main()
{
    srand(time(0));
    int Number = 5, N = Number-1, temp=0;
    bool isSort = true;
    int Tab[Number][2];
    for (int i =0; i< Number; i++)
    {
        Tab[i][0] = rand()%6;
        Tab[i][1] = i;
        //cout << Tab[i][0] << ", " << Tab[i][1] << endl;
    }
        for (int i =0; i<Number-1; i++)
    {    
            N = Number-1;
            isSort = true;
            while (N>i)
            {
                if (Tab[N][0]<Tab[N-1][0])
                {
                    temp = Tab[N][0];
                    Tab[N][0] = Tab[N-1][0];
                    Tab[N-1][0] = temp;
                    temp = Tab[N][1];
                    Tab[N][1] = Tab[N-1][1];
                    Tab[N-1][1] = temp;
                    isSort = false;
                } 
                N-=1;
            }
            if (isSort == true)
            {
                break;
            }
    }
    cout << "\n sorted array: " << endl;
    for (int i =0; i < Number; i++)
    {
        cout << "[" << Tab[i][0] << ", " << Tab[i][1] << "]" << endl;
    }
    cout << "\n deleting element from sorted array: "<<endl;
    int Pos = 2, Temp1, Temp2; //choose index of deleting element 
    for (int i=Pos+1; i<Number; i++)
    {
        temp = Tab[i][0];
        Tab[i][0] = Tab[i-1][0];
        Tab[i-1][0] = temp;
        temp = Tab[i][1];
        Tab[i][1] = Tab[i-1][1];
        Tab[i-1][1] = temp;
    }
    Number -=1;
    int NTab[Number][2];
    for (int i=0; i<Number; i++)
    {
        NTab[i][0] = Tab[i][0];
        NTab[i][1] = Tab[i][1];
    }
    //delete [] Tab;
    //Tab[Number][2] = NTab;
    for (int i =0; i< Number; i++)
    {
        cout << NTab[i][0] << ", " << NTab[i][1] << endl;
    } 

    cout << "\n adding element to sorted array: "<<endl;
    int x= 22, y = 100; // we whant to add 
    Number += 1;
    //int TempTab[Number+1][2] = Tab; ->doesnt working ://, lests try it longer way
    int NewTab[Number][2];
    for (int i=0; i<Number-1; i++)
    {
        NewTab[i][0] = Tab[i][0];
        NewTab[i][1] = Tab[i][1];
    }
    NewTab[Number-1][0] = x;
    NewTab[Number-1][1] = y;
    int j = Number-1;
    while (j > Pos)
    {
        temp = NewTab[j][0];
        NewTab[j][0] = NewTab[j-1][0];
        NewTab[j-1][0] = temp;
        temp = NewTab[j][1];
        NewTab[j][1] = NewTab[j-1][1];
        NewTab[j-1][1] = temp; 
        j--;
    }
    for (int i =0; i< Number; i++)
    {
        cout << NewTab[i][0] << ", " << NewTab[i][1] << endl;
    }  
    return 0;
}