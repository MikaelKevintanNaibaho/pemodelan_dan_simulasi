#ifndef M_M_1_H
#define M_M_1_H

#include "lcgrand.h"
#include <math.h>
#include <stdio.h>

#define Q_LIMIT 100 // limit on qeueu lenght
#define BUSY 1
#define IDLE 0

extern int next_event_type;
extern int num_custs_delayed;
extern int num_delays_required;
extern int num_events;
extern int num_in_q;
extern int server_status;


extern float area_num_in_q;
extern float area_server_status;
extern float mean_interarrival;
extern float mean_service;
extern float sim_time;
extern float time_arrival[Q_LIMIT + 1];
extern float time_last_event;
extern float time_next_event[3];
extern float total_of_delays;

extern FILE *infile, *outfile;


void initialize(void);
void timing(void);
void arrive(void);
void depart(void);
void report(void);
void update_time_avg_stats(void);
float expon(float mean);

#endif // M_M_1_h