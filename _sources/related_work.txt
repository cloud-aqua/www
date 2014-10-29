Related Work
======================================================================

Physical Component Failure Characterization in Datacenters
----------------------------------------------------------------------

Several studies have characterized the failures of servers (or computing
nodes in general) and in datacenter networks (DCNs),

-  P . Gill, N. Jain, and N. Nagappan, "Understanding Network Failures
   in Data Centers: Measurement, Analys is , and Implications," SIGCOMM,
   2011 - the authors studied the reliability of DCNs by analyzing error
   logs and found that the ToR and aggregation switches are highly
   reliable, while the load balancers experience a high number of
   failures. In addition, network redundancy helps but cannot completely
   mitigate all failures
-  B. Schroeder and G. a Gibson, "A Large-Scale Study of Failures in
   High-Performance Computing Systems," IEEE Trans. Dependable Secur.
   Comput., vol. 7, no. 4, pp. 337-350, Oct. 2010. - the authors studied
   various types of failures in HPC clusters, their failure rates, mean
   time between failure (MTBF) and mean time to repair (MTTR). It was
   found that the most frequent failure is hardware failure, and MTBF is
   best modeled by Weibull distribution
-  K. V. Vishwanath and N. Nagappan, "Characterizing cloud computing
   hardware reliability," Proc. 1st ACM Symp. Cloud Comput. - SoCC '10,
   p. 193, 2010. - Characterized server failures and hardware repairs in
   a large datacenter, and showed the relationship between successive
   failures on the same physical server

Only a few papers have studied, to a limited extent, the correlation
between failures,

-  R. K. Sahoo, M. S. Squillante, and a. Sivasubramaniam, "Failure data
   analysis of a large-scale heterogeneous server environment," Int.
   Conf. Dependable Syst. Networks, 2004, pp. 772781, 2004. - Reports
   correlation between the type of workload and failure rate
-  
-  R. K. Iyer, D. J. Rossetti, and M. C. Hsueh, "Measurement and
   modeling of computer reliability as affected by system activity," ACM
   Trans. Comput. Syst., vol. 4, no. 3, pp. 214-237, Aug. 1986 - Studies
   correlation between workload intensity and failure rate.
-  B. Schroeder and G. a Gibson, "A Large-Scale Study of Failures in
   High-Performance Computing Systems," IEEE Trans. Dependable Secur.
   Comput., vol. 7, no. 4, pp. 337-350, Oct. 2010 - shows that some
   spatial correlation exists among network failures, and the number of
   failures observed in one time interval (at daily, weekly and monthly
   granularities) was found to predict the number of failures expected
   in the next time interval.
-  B. Schroeder and G. A. Gibson, "Disk failures in the real world: what
   does an MTTF of 1,000,000 hours mean to you?," in FAST '07
   Proceedings of the 5th USENIX conference on File and Storage
   Technologies, 2007, p. 1 - A similar observation was also made

Component Failure Data, and Application Workload and Performance
----------------------------------------------------------------------

Reliability and Availability Models and Analysis
----------------------------------------------------------------------

Resource (VM) Provisioning and Allocation Strategies
----------------------------------------------------------------------


