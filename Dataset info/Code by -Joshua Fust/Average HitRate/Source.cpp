#include<fstream>
using namespace std;
#include<iostream>

int main() {
	ifstream file("result.txt");
	string x;
	float y;
	float total=0;
	float average;
	while (file >> x >> y) {
		total = total + y;
	}
	average = total / 100;
	cout << average;

	return 0;
}