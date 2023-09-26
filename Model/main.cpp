// WormSim main.

#include <stdio.h>
#include <time.h>
#include "wormsim.h"

int main(int argc, char *argv[])
{
	init();
	for (int i = 0; i < 1000; i++)
	  {
	    step(0.0);
	    double a = get_segment_angle(0);
	    double m = get_ventral_motor_activation(0);
	    double m2 = get_ventral_muscle_activation(0);
	    printf("angle=%f, motor=%f, muscle=%f, time=%d\n",a,m,m2,time(0));
	  }
	term();
	return 0;
}
