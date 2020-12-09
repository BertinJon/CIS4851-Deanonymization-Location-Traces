#include<iostream>
#include<fstream>
#include<string>
#include <stdlib.h>
#include<sstream>
using namespace std;


int main() {
	ifstream input("RegionCenters.txt");
	ofstream output("regions.txt");
	string regions[691], templine,fullRegion[691],regionLat[691],newRegion[691];
	int counter;
	for (int i = 0; i < 691; i++) {
		getline(input, templine);
		fullRegion[i] = templine;
		for (int j = 0; j < templine.size() - 1; j++) {
			if (templine.at(j) == '_') {
				counter = j;
				break;
			}
		}
		templine.resize(counter);
		regions[i] = templine;
	}
	for (int i = 0; i < 691; i++) {
		string temp = "";
		counter = 0;
		templine = fullRegion[i];
		for (int j = 0; j < templine.size(); j++) {
			if (counter == 2) {
				temp = temp + templine.at(j);
			}
			if (templine.at(j) == '_') {
				counter++;
			}
		}
		regionLat[i] = temp;
	}
	counter = 0;
	for (int i = 0; i < 691; i++) {
		stringstream ss(regionLat[i]);
		float x;
		ss >> x;
		if (x < 45) {
			counter++;
			output << fullRegion[i]<<endl;
		}
	}
	cout << counter << endl;
	return 0;
}