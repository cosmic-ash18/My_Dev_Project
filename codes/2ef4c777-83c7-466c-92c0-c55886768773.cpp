#include <iostream>
using namespace std;
 
int main()
{
    ios :: sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
 
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for(int i = 0; i < n; i++)
        cin >> arr[i];
        for(int i = 0; i < n; i++)
        {
            int start = 1, end = i+1, mid = (start+end)/2;
            while(start <= end)
            {
                if(arr[i+1-mid] >= mid)
                start = mid+1;
                else
                end = mid-1;
                mid = (start+end)/2; 
            }
            cout << end << " ";
        }
        cout << "\n";
    }
}