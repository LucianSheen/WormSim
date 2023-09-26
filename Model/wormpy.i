/* File: wormpy.i */
%module wormpy

%{
#define SWIG_FILE_WITH_INIT
#include "wormsim.h"
%}

// wormsim API.
int init();
void set_steering_synapse_weight(int synapse, double weight);
void step(double salt_stimulus);
double get_steering_activation(int neuron);
double get_dorsal_motor_activation(int segment);
double get_ventral_motor_activation(int segment);
double get_dorsal_muscle_activation(int segment);
double get_ventral_muscle_activation(int segment);
double get_body_point(int index);
double get_segment_angle(int segment);
void term();
