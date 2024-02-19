#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<ostream>
#include<istream>
#include<fstream>
#include<random>

using namespace std;
//string DIRECTORY_NAME = "history.txt";
double M, C, b, N, C_suppose, total_limit,C_average;
double S;
double solve_second(double A, double B, double C) {
	double delta = B * B - 4 * A * C;
	if (delta < 0||A==0)return 0;
	else return(-B + sqrt(delta)) / (2 * A);
}
void compute(int i = 0) {
	if (i == 0) {//×ã¹»¶àÇ®
		double X1 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - M * (N + 1), C * C - M * C + M * b);
		double X2 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - M * N, C * C - M * C + M * b);
		double E1 = (X1+b) * ((M / ((N + 2) * X1 + C)) - 1);//Æ½ºâµã
		double E2 = (X2+b) * ((M / ((N + 1) * X2 + C)) - 1);
		if (E2 < 0)return;
		printf("M=%.0lf,C=%.0lf(%.0lf),b=%.0lf\n", M, C, C / C_average, b);
		printf("Result:   X1=%.3lf, X2=%.3lf, E1=%.3lf, E2=%.3lf,percent1=%.3lf%,percent2=%.3lf percent=%.3lf%\n", X1+b, X2+b, E1, E2, E1 * 100 / (X1+1), E2 * 100 / (X2+1), 50 * E2 / E1);
	}
	else if (i == 1) {
		double X1 = C_suppose - b, X2 = 2 * C_suppose - b;
		double X11 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - M * (N + 1), C * C - M * C + M * b);
		double X22 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - M * (N ), C * C - M * C + M * b);
		if (X1 > X11) {
			X1 = X11; return;
		}
		else
			X11 = solve_second(N * N, 2 * (C + 2 * X1) * N - M * (N - 1), (C + 2 * X1) * (C + 2 * X1) - M * (C + 2 * X1) + M * b);
		if (X2 > X22) {
			X2 = X22;
		}
		else
			X22= solve_second(N * N, 2 * (C + X2) * N - M * (N - 1), (C + X2) * (C + X2) - M * (C + X2) + M * b);
		double E1 = (X1+b) * ((M / (N * X11 + C + 2 * X1)) - 1);
		double E2 = (X2 + b) * ((M / (N * X22 + C +  X2)) - 1);
		if (E2 < 0)return;
		printf("M=%.0lf,C=%.0lf(%.0lf),b=%.0lf\n", M, C,C/C_average, b);
		printf("Result:   X11=%.2lf,X22=%.2lf, C_suppse=%.2lf, X1=%.2lf,X2=%.2lf,E1=%.3lf(%.3lf%%), E2=%.3lf(%.3lf%%), percent=%.3lf%%\n",
						X11 + b, X22 + b, C_suppose, X1 + b, X2 + b, E1, E1 * 100 / (X1 + b), E2, E2 * 100 / (X2 + b), 50 * E2 / E1);
	}
}
void compute2(int i = 0) {
	if (i == 0) {
		double X1 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S, C * C - S * C + M);
		double X2 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, C * C - S * C + M);
		double E1 = ((M / X1) + S) * X1 / ((N + 2) * X1 + C) - X1 - b;
		double E2 = ((M / X2) + S) * X2 / ((N + 1) * X2 + C) - X2 - b;
		if (E2 < 0)return;
		printf("M=%.0lf,S=%.0lf,C=%.0lf,b=%.0lf\n", M, S, C, b);
		printf("Result:   X1=%.3lf, X2=%.3lf, E1=%.3lf, E2=%.3lf,percent1=%.3lf%,percent2=%.3lf percent=%.3lf%\n", X1, X2, E1, E2, E1 * 100 / (X1 + b), E2 * 100 / (X2 + b), 50 * E2 / E1);
	}
	else if (i == 1) {
		double X1 = C_suppose - b, X2 = 2 * C_suppose - b;
		double X11 = solve_second((N + 2) * (N + 2), 2 * C * (N + 2) - (N + 1) * S, C * C - S * C + M);
		double X22 = solve_second((N + 1) * (N + 1), 2 * C * (N + 1) - N * S, C * C - S * C + M);
		if (X1 > X11) {
			X1 = X11;
			return;
		}
		else {
			X11 = solve_second(N * N, 2 * (C + 2 * X1) * N - (N - 1) * S,
				(C + 2 * X1) * (C + 2 * X1) - S * (C + 2 * X1) + M);
		}
		if (X2 > X22) {
			X2 = X22;
		}
		else {
			X22 = solve_second(N * N, 2 * (C + X2) * N - (N - 1) * S,
				(C + X2) * (C + X2) - S * (C + X2) + M);
		}
		double E1 = ((M / X1) + S) * X1 / (N * X11 + C + 2 * X1) - X1 - b;
		double tmp = M / X2;
		tmp = tmp + S;
		tmp = tmp * X2;
		double tmp1 = N * X22 + C + X2;
		tmp = tmp / tmp1;
		double E2 = ((M / X2) + S) * X2 / (N * X22 + C + X2) - X2 - b;
		if (E2 < 0)return;
		printf("M=%.0lf,S=%.0lf,C=%.0lf,b=%.0lf\n", M, S, C, b);
		printf("Result:   X11=%.3lf,X22=%.3lf, C_suppse=%.3lf, X1=%.3lf,X2=%.3lf,E1=%.3lf(%.3lf%%), E2=%.3lf(%.3lf%%), percent=%.3lf%%\n",
			X11 + b, X22 + b, C_suppose, X1 + b, X2 + b, E1, E1 * 100 / (X1 + b), E2, E2 * 100 / (X2 + b), 50 * E2 / E1);
	}
}
int main() {
	freopen("easy.txt", "w", stdout);
	{//our  MX/(X-b)
		b = 1; C = 19 * 98; C_suppose = 20; total_limit = 3000; C_average = 19;M = 2040;
		printf("MX/(X-b)  very rich\n");
		for (int i = 0; i <= 98; i++) {
			N = i; C = (98 - i) * 19;
			compute();
		}
		printf("\n\n\n\nMX/(X-b)  not rich\n");
		for (C_suppose = 1; C_suppose < 50; C_suppose++) {
			for (int i = 0; i <= 98; i++) {
				N = i; C = (98 - i) * 19;
				compute(1);
			}
		}
	}
	{//our  M/X+S
		b = 1; C = 19 * 98; C_suppose = 20; total_limit = 3000;S = 3000, M = 0;
		/*printf("\n\n\n\nM/X + S  S,M choose\n");
		for (S = 0; S <= 3000; S += 50) {
			M = 3000 - S;
			for (int i = 0; i <= 98; i++) {
				N = i; C = (98 - i) * 19;
				compute2();
			}
		}
		printf("\n\n\n\nM/X + S  S,M special choose\n");
		for (S = 0; S <= 3000; S += 50) {
			M = 3000 - S;
			for (int i = 0; i <= 0; i++) {
				N = i; C = (98 - i) * 19;
				compute2();
			}
		}*/
		S = 2100, M = 900;
		printf("\n\n\n\nM/X + S  very rich\n");
		for (int i = 0; i <= 98; i++) {
			N = i; C = (98 - i) * 19;
			compute2();
		}
		printf("\n\n\n\nM/X + S  not rich\n");
		for (C_suppose = 1; C_suppose < 50; C_suppose++) {
			for (int i = 0; i <= 98; i++) {
				N = i; C = (98 - i) * 19;
				compute2(1);
			}
		}
	}
}

