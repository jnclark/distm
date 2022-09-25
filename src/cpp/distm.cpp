#include <cmath>

// Note: euclidean distance between points is calculated via
// std::sqrt(x*x + y*y) etc. The safer std::hypot function has been
// replaced for the sake of more speed (with the cost being overflow
// is not checked. Do be careful).

// Distance functions

float distance(float a, float b) {
  return std::sqrt(a*a + b*b);
}

float distance(float a, float b, float c) {
  return std::sqrt(a*a + b*b + c*c);
}

// Two dimensional functions

extern "C"
void distm(float* points, int num_points, int dim, float* dist_matrix) {
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1]);
    } 
  }
}

extern "C"
void distm_parallel(float* points, int num_points, int dim, float* dist_matrix) {
#pragma omp parallel for schedule(dynamic) //static
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1]);
    } 
  }
}

// Three dimensional functions

extern "C"
void distm3d(float* points, int num_points, int dim, float* dist_matrix) {
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1], points[i*dim+2] - points[j*dim+2]);
    } 
  }
}

extern "C"
void distm3d_parallel(float* points, int num_points, int dim, float* dist_matrix) {
#pragma omp parallel for schedule(dynamic) //static
  for (int i = 0; i < num_points; i++) {
    for(int j = i; j < num_points; j++) {
      dist_matrix[i*num_points + j] = dist_matrix[j*num_points + i] = distance(points[i*dim] - points[j*dim], points[i*dim+1] - points[j*dim+1], points[i*dim+2] - points[j*dim+2]);
    } 
  }
}
