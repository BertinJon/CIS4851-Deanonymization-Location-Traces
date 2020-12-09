using namespace std;
#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<stdlib.h>
#include<time.h> 

int iter=1; //global counter for userID
string user[100];

void setUser() {
	string userIntro = "user_000";
	for (int i = 0; i < 100; i++) {
		string userID;
		stringstream ss;
		if (iter < 10) {
			ss << iter;
			ss >> userID;
			user[iter - 1] = userIntro + "00" + userID;
		}
		else if (iter < 100) {
			ss << iter;
			ss >> userID;
			user[iter - 1] = userIntro + "0" + userID;
		}
		else if (iter < 1000) {
			ss << iter;
			ss >> userID;
			user[iter - 1] = userIntro + userID;
		}
		iter++;
	}

}

int main() {
	ifstream centers("region.txt");
	string regions[586],templine;
	int counter;
	for (int i = 0; i < 586; i++) {
		getline(centers, templine);
		for (int j = 0; j < templine.size() - 1; j++) {
			if (templine.at(j) == '_') {
				counter = j;
				break;
			}
		}
		templine.resize(counter);
		regions[i] = templine;
	}


	ofstream inputfile;
	ifstream externaltraj("externaltraj.txt");
	string outputfilename,cityName;
	srand(time(0));
	int randomtime, random, randomlen, time1, time2;
	setUser();
	string userLOC[100][10];
	for (int k = 0; k < 100; k++) {
		stringstream ssname;
		string tempname = "user";
		string number,xtraj;
		ssname << (k + 1);
		ssname >> number;
		outputfilename = tempname + number +".txt";
		inputfile.open(outputfilename);
		time1 = rand() % 182;
		time2 = rand() % 182;
		getline(externaltraj, xtraj);
		inputfile << user[k] << ";|" << time1<<"," <<xtraj<<"|"<< time2<<","<<xtraj<<"|"<<endl;
		for (int i = 0; i < 100; i++) {
			inputfile << user[i] << ";|";
			randomlen = rand() % 10 + 1;
			for (int j = 0; j < randomlen; j++) {
				stringstream ss;
				string timestamp;
				randomtime = rand() % 182;
				ss << randomtime;
				ss >> timestamp;
				inputfile << timestamp << ",";
				random = rand() % 586;
				userLOC[i][j] = regions[random];
				inputfile << userLOC[i][j] << "|";
			}
			inputfile << endl;
		}
		inputfile.close();
	}

	return 0;
}