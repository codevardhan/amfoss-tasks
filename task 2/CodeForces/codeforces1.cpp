    #include <iostream>
    #include <algorithm>
     
    using namespace std;
     
    int main()
    {
    	int n, m, a;
    	cin >> n >> m >> a;
     
    	int widthBlocks = n / a + (n % a != 0 ? 1 : 0);
    	int heightBlocks = m / a + (m % a != 0 ? 1 : 0);
     
    	cout << widthBlocks * heightBlocks << endl;
     
    	return 0;
    }
