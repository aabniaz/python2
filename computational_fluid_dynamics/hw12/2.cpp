#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;


const double start_x = 0, end_x = 1;
const double dx = 0.001, dt = 0.001;
const double eps = 1e-6;
const double u = 1; 
const int N = (end_x - start_x) / dx + 1;
const int stop_iteration = 1e6;
double U_old[N], U_new[N], x[N];


double find_absolute_max(){
    double maximum = 0;
    for(int i = 0; i < N; ++i){
        if(abs(U_new[i] - U_old[i]) > maximum){
            maximum = abs(U_new[i] - U_old[i]);
        }
    }
    return maximum;
}


int main(){
    auto start = high_resolution_clock::now();

    for(int i = 0; i < N; ++i){
        x[i] = start_x + i*dx;
    }
    
    // U(t=0, x) = 0
    for(int i = 0; i < N; ++i){
        U_old[i] = 0;
    }

    int row = 2;
    double maximum = 0;
    
    do{ 
        for(int i = 1; i < N-1; ++i){
            U_new[i] = 0.5 * (U_old[i+1] + U_old[i-1]) - 0.5*dt/dx * ((U_old[i+1]*U_old[i+1])/2 - (U_old[i-1]*U_old[i-1])/2);
        }

        // U(t, x=0) = 1
        // U(t, x=1) = 0
        U_new[0] = 1;
        U_new[N-1] = 0;

        maximum = find_absolute_max();

        for(int i = 0; i < N; ++i){
            U_old[i] = U_new[i];
        }
        row++;
    }while(maximum > eps and row < stop_iteration);

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    printf("calculating time: %.6f seconds\n", duration.count() / 1e6);
    cout << row << endl;

    FILE *File;
    File = freopen("u_upd_1_cpp.txt", "w", stdout);
    for(int i = 0; i < N; ++i){
        if(i == N - 1){
            printf("%.6f", U_new[i]);
        }else{
            printf("%.6f\t", U_new[i]);
        }
    }
    fclose(File);

    File = freopen("x_upd_1_cpp.txt", "w", stdout);
    for(int i = 0; i < N; ++i){
        if(i == N - 1){
            printf("%.6f", x[i]);
        }else{
            printf("%.6f\t", x[i]);
        }
    }
    fclose(File);

    return 0;
}