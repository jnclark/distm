#include <cmath>

float distance(float a0, float a1, float b0, float b1) {
  return std::hypot(a0-b0, a1-b1);
}

extern "C"
void distm(float* points, int num_points, int dim, float* dist_matrix) {
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim], points[i*dim+1],points[j*dim], points[j*dim+1]);
    } 
  }
}

extern "C"
void distm_parallel(float* points, int num_points, int dim, float* dist_matrix) {
#pragma omp parallel for schedule(dynamic) //static
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim], points[i*dim+1],points[j*dim], points[j*dim+1]);
    } 
  }
}
