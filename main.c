#include "lcgrand.h"
#include "m_m_1.h"
#include <math.h>
#include <stdio.h>

int next_event_type;
int num_custs_delayed;
int num_delays_required;
int num_events;
int num_in_q;
int server_status;

float area_num_in_q;
float area_server_status;
float mean_interarrival;
float mean_service;
float sim_time;
float time_arrival[Q_LIMIT + 1];
float time_last_event;
float time_next_event[3];
float total_of_delays;

FILE *infile;
FILE *outfile;


int main(void) {
	/* Open input and output files. */
	  infile  = fopen("../../mm1.in", "r");
	  outfile = fopen("mm1.out", "w");

	  /* Specify the number of events for the timing function */
	  num_events = 2;

	  /* Read input parameters */
	  fscanf(infile, "%f %f %d", &mean_interarrival, &mean_service, &num_delays_required);

	  /* Write report heading and input parameters */
	  fprintf(outfile, "Single server queuing system\n\n");
	  fprintf(outfile, "Mean interarrival time%11.3f minutes \n\n", mean_interarrival);
	  fprintf(outfile, "Mean service time%16.3f minutes\n\n", mean_service);
	  fprintf(outfile, "Number of customers%14d\n\n", num_delays_required);

	  /*Initialize the simulation */
	  initialize();

	  /* Run the simulation while more delays are still needed */
	  while(num_custs_delayed <  num_delays_required){
		  /*Determine the next event */
		  timing();

		  /* Update time-average statistical accumulators. */
		  update_time_avg_stats();

		  /* Invoke the appropriate event function */
		  switch(next_event_type){
			  case 1:
				  arrive();
				  break;
			  case 2:
				  depart();
				  break;
		  }
	  }

	  /* Invoke the report generator and end the simulation */
	  report();

	  fclose(infile);
	  fclose(outfile);

	  return 0;
}