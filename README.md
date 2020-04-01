1. Suyash Sharma (ss2967), Mohit Pavecha (mp1379)

2. I implemented a nested functionality after making use of try and except with a socket.timeout method. Since it was a nested functionality, the load balancer would first search in TS1 for the URL. If it gets no response within 1 second, it would make the same query to TS2. If it doesn't get a response in a second, it would just return the error string. The timeout were kept short because I used a HashMap in both TS1 and TS2 (which has a constant lookup time) that guranteed a response within a second, provided the URL existed in that specific server.

3. No issues that I know of. The code is working perfectly fine as in Project Description.

4. Since the current project is a follow-up for Project - 1, I feel there was a lot of time gap between the two projects and I had almost forgotten how I implenmented my previous code functionality. So one major challenge was to go through the code base again and try understand what it was previously doing and make changes to it so it satisfies the requirements of Project - 2. Another issues was implementation of ls.py as I was kind of confusing at first but really intuitive when I realized I could use try and except block to catch whether a server contains the IP Address of a URL or it does not.

5. A little bit more of Python and how the DNS Lookup work. More specifically, in what different ways you can implement try and except blocks. How to handle multiple socket connections.


The programs must work with the following command lines:
python ts1.py ts1ListenPort
python ts2.py ts2ListenPort
python ls.py lsListenPort ts1Hostname ts1ListenPort ts2Hostname ts2ListenPort
python client.py lsHostname lsListenPort
