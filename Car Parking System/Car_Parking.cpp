#include <iostream>
#include <set>
using namespace std;

int main()
{
    int u_input;
    int amount=0,Count=0;
    int tkn;

    set <int> reserved, booked;

    for(int i = 1; i <= 50; i++)
        reserved.insert(i);
    int token = *reserved.begin();

    while(true)
    {
        cout << "\t\t\t\t\t\t\t\tPress 1 To Park Your Car" << endl;
        cout << "\t\t\t\t\t\t\t\tPress 2 To know the record" << endl;
        cout << "\t\t\t\t\t\t\t\tPress 3 for Departure\n" << endl;
        cout << "\t\t\t\t\t\t\t\tCHOOSE AN OPTION: ";
        cin >> u_input;

        if (u_input == 1)
        {
            if (Count<=50)
            {
                amount = amount + 100;
                Count++;
                cout << "\t\t\t\t\t\t" << string(65, '=') << endl;
                cout << "\t\t\t\t\t\t\t\tYour Vehicle is successfully parked.\n\t\t\t\t\t\t\t\tYOUR TOKEN NUMBER IS: " << token << endl;
                cout << "\t\t\t\t\t\t" << string(65, '=') << endl << endl;
                reserved.erase(token);
                booked.insert(token);
                token = *reserved.begin();
            }
            else
                cout<<"no more cars,parking is full"<<endl;
        }
        else if(u_input == 2)
        {
            cout << "\t\t\t\t\t\t" << string(65, '=') << endl;
            cout << "\t\t\t\t\t\t\t\tThe total amount: " << amount << endl;
            cout << "\t\t\t\t\t\t\t\tThe total of vehicles parked: " << Count << endl;
            cout << "\t\t\t\t\t\t\t\tRemaining Parking Slots: " << 50-Count << endl;
            cout << "\t\t\t\t\t\t" << string(65, '=') << endl << endl;
        }
        else if(u_input == 3)
        {
            cout << "\n\t\t\t\t\t\t\t\tEnter Your Token Number: ";
            cin >> tkn;
            if(booked.count(tkn))
            {
                cout << "\t\t\t\t\t\t" << string(65, '=') << endl;
                cout<<"\t\t\t\t\t\t\t\t\tRECORD DELETED"<<endl;
                cout << "\t\t\t\t\t\t" << string(65, '=') << endl <<endl;
                booked.erase(tkn);
                Count--;
                amount -= 100;
            }
            else
                cout << "\t\t\t\t\t\t\t\tINVALID TOKEN NUMBER\n\n";
        }
        else
        {
            cout<<"\t\t\t\t\t\t\t\tINVALID OPTION"<<endl;
        }
    }
}
