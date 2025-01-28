# Brief aside

This is some object oriented code in order to model a particular type of dynamic graph. 

Intuitively: suppose we have a game where n people say who their friends are at the end of each timestep. We suppose that if you put a group of people in a room they interact more hence they are more likely to make friends (but also those friendships are also more likely to die). Triadic closure also acts (this Suppose A+B means A is friends with B then A+B, B+C => A+C at least it increases the probability).

My question is: if I allow you to control the rooms they are in, what is the best way to do it in order to maximise or minimise friendships? 


Currently this code can succesfully produce these simualations but the viz is not working. Some statistics and analytics have been implemented.





# What I want 

**Graph current state** 
- historic states 
- pertubation event history 
- *I believe this will be handled by DyNetX* 

**Graph dynamics engine** 
- triadic closure 
- stochastic randomness 
- homophily 
- kiromoto model 
- fear of the other side powered by lack of interaction 

**Stochastic Pertubation Event (SPE) Driver** 
- choosing which SPE to activate 

**Initial graph state** 

**Graph visualisation** 

**Measurable topological properties** 
- clustering 
- polarisation when considering homophily models 

# TODO 
- make the active graphs update in teh change_driver function 
- check that the graphSPEModel works 
- make simplest possible test functions for graph dynamics engine and SPE drivers 
- try and initialise the polarisation example 
