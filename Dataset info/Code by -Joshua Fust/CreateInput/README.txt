This code needs externaltraj.txt and region.txt to run.

It outputs 100 files starting at user1 to user100 and is used as the input for the de-anonymization algorithms.

This code takes in the list of external trajectories and regions to output properly formatted input for the de-anonymization algorithms
The input is a list of 100 users along with the external trajectory for 1 user and for the 100 users there random path around Michigan is created.
The UP is excluded from the randomized path to limit the area for the algorithm to check. Each user region is accompanied by a time code that is randomly generated.

