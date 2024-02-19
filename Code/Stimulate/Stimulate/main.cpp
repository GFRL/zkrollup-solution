//#define _CRT_SECURE_NO_WARNINGS
//#include<iostream>
//#include<cstdio>
//#include<algorithm>
//#include<cmath>
//#include<string>
//#include<ostream>
//#include<istream>
//#include<fstream>
//#include<random>
//
//using namespace std;
////string DIRECTORY_NAME = "history.txt";
//uniform_int_distribution<int> u(0, 100000);
//default_random_engine e(1945);
//string FILE_NAME = "tmp.txt";
//fstream o;
//int total_cnt, cnt;
//double A[1001];//用于存放财富
//double A_init[1001];
//double B[1001];
//double B_init[1001];
//double p[1001];//存放本次结果
//double b=100;//存放门槛
//double value[1001];
//double M=100;
//int Num;
//int choice=0;
//double first[100] = { 2,2000,2000 };
//double pre_sum;
//double p_sum;
//void init() {
//	double sum = 0;
//	for (int i = first[0]+1; i <= Num; i++) {
//		A[i] = u(e); sum += A[i];
//	}
//	double all = 10000;
//	for (int i = 1; i <= first[0]; i++) {
//		B_init[i] = B[i] = first[i]/10000;
//		A_init[i] = A[i] = first[i];
//		all -= first[i];
//	}
//	for (int i = first[0]+1; i <= Num; i++) {
//		
//		A_init[i] = A[i] = (A[i] / sum) * all;
//		B_init[i] = B[i] = A[i] / 10000;
//	}
//	pre_sum = sum;
//}
//void output(int u=0) {
//	if (u == 1) {
//		for (int i = 1; i <= Num; i++) {
//			printf("A[%d]=%.4lf->%.4lf, B[%d]=%.3lf%->%.3lf% \n", i, A_init[i], A[i], i, B_init[i] * 100, B[i] * 100);
//		}
//		return;
//	}
//	printf("Now %d loop:", cnt);
//	for (int i = 1; i <= Num; i++) {
//		printf("A[%d]=%.4lf, B[%d]=%.3lf% \n", i, A[i], i, B[i] * 100);
//	}
//}
//void P() {
//	for (int i = 1; i <= Num; i++)
//		p[i] = (u(e) * 1.0 / 100000) * A[i];
//		//printf("p[%d]=%.3lf\n", i, p[i]);
//}
//void choose() {
//	choice = -1;
//	double sum = 0;
//	for (int i = 1; i <= Num; i++)
//		if (p[i] > 5*b) {
//			choice = choice;
//			sum += p[i] - b;
//			p[i] -= b;
//		}
//		else
//			p[i] = 0;
//	p_sum = sum;
//	double target = (u(e)*1.0 / 100000) * sum;
//	for (int i = 1; i <= Num; i++) {
//		if (p[i] == 0)continue;
//		if (target <= p[i]) {
//			choice = i; return;
//		}
//		else {
//			target -= p[i];
//		}
//	}
//}
//void renew() {
//	double sum = 0;
//	for (int i = 1; i <= Num; i++) {
//		//A[i] *= 0.999999999;
//		//A[i] += M*p[i]/ p_sum;
//		sum += A[i];
//	}
//
//	if (choice == -1) {
//		printf("No one get it!\n");
//	}
//	else {
//		//printf("User %d get %.3lf!\n", choice, M*(1+ b/p[choice]));
//		//our solution
//		/*A[choice] += M * (1 + b / p[choice]);
//		sum += M * (1 + b / p[choice]);*/
//		//pow solution
//		A[choice] += M;
//		sum += M;
//	}
//	for (int i = 1; i <= Num; i++) {
//		B[i] = A[i] / sum;
//	}
//	pre_sum = sum;
//	//output();
//}
//int main() {
//	//freopen("12.txt", "w", stdout);
//	
//	cin >> total_cnt>>Num;
//	b = b / Num;
//	init();
//	output();
//	while (cnt < total_cnt) {
//		cnt++;
//		P();
//		choose();
//		renew();
//		//cout << pre_sum << endl;
//	}
//	output(1);
//}
//
