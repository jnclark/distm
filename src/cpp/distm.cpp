#include <cmath>

// Note: euclidean distance is calculated via the standard library's
// std::hypot function.

// Two dimensional functions

extern "C"
void distm(float* points, int num_points, int dim, float* dist_matrix) {
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = std::hypot(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1]);
    } 
  }
}

extern "C"
void distm_parallel(float* points, int num_points, int dim, float* dist_matrix) {
#pragma omp parallel for schedule(dynamic) //static
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = std::hypot(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1]);
    } 
  }
}

// Three dimensional functions

extern "C"
void distm3d(float* points, int num_points, int dim, float* dist_matrix) {
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
            dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = std::hypot(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1], points[i*dim+2] - points[j*dim+2]);
    } 
  }
}

extern "C"
void distm3d_parallel(float* points, int num_points, int dim, float* dist_matrix) {
#pragma omp parallel for schedule(dynamic) //static
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
            dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = std::hypot(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1], points[i*dim+2] - points[j*dim+2]);
    } 
  }
}
