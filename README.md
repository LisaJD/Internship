# Internship

ART applied to non-numerical inputs
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7442567

https://medium.com/@brianray_7981/tutorial-write-a-finite-state-machine-to-parse-a-custom-language-in-pure-python-1c11ade9bd43


http://mcts.ai/pubs/mcts-survey-master.pdf
http://www.cs.huji.ac.il/~ai/projects/2013/UlitmateTic-Tac-Toe/

https://www.codeproject.com/Articles/22769/Introduction-to-Object-Oriented-Programming-Concep
Resources on concurrency in testing:
https://ieeexplore.ieee.org/document/5954385/

https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml

https://pdfs.semanticscholar.org/a158/b0ec69344d7e69513807d94d193e17b664bf.pdf

The oracle problem: https://ieeexplore.ieee.org/document/6963470/

https://mostafa-samir.github.io/Tic-Tac-Toe-AI/

Copy constructor in Python:
(purpose = to copy an argument and pass as an argument to a function, so you can get all the properties of that object)

class Foo:
    def __init__(self, orig=None):
        if orig is None:
            self.non_copy_constructor()
        else:
            self.copy_constructor(orig)
    def non_copy_constructor(self):
        # do the non-copy constructor stuff
    def copy_constructor(self, orig):
        # do the copy constructor

a=Foo()  # this will call the non-copy constructor
b=Foo(a) # this will call the copy constructor


*Template Method
Import code from existing classes, but with ability to
override any you need to.

Decorators
Extends functionality of a function without modifying it

Nested functions = functions defined inside
functions. They are not available outside of the parent scope

• Proxy
-	Class that functions as an interface to something else (eg. A network connection, file, resource that you don’t want to duplicate) 
-	Can incorporate caching

• Virtual Proxy
-	Creates a skeleton of an expensive resource/object to speed up applications (so don’t need to load it each time resource asked for)

• Lazy Initialization
-	Delaying creation of an object until first needed. First uses accessor method to check if cache already exists, if not creates it when requested.
-	For example, in the state machine program: 
•Design Patterns
-	Abstraction. How to solve an entire class of similar problems
-	Purpose = to separate things that change from things that stay the same
-	Vector of change = most important thing that changes in your program/greatest cost
-	3 categories based on purpose: behavioural (state machine falls under behavioural?), structural, creational
• Singleton
-	Makes a private nested inner class, in Python by prefixing with double underscore
-	Put inside it everything you would normally put in a class
• __getattr__() method
(Access comes through delegation, using the __getattr__( ) method to redirect calls to the single instance.)

-	You should be able to define a static table in each State subclass that defines the transitions in terms of the other State objects. However, it turns out that this approach generates cyclic initialization dependencies. To solve the problem, I’ve had to delay the initialization of the tables until the first time that the next( ) method is called for a particular State object.
 
Python Object Oriented Programming

• Magic Methods
-	Not manually invoked, Python automatically invokes them
-	Includes: __init__, the object initializer ; __str__ which provides a string representation of your object ; __add__ which allows you to overload the + operator (?)
-	How to use: NOT obj.__str__() but str(obj)
• __getattr__ = catch all for methods that don’t exist, does a default action for all non-existent methods
• __getattribute__ = default method that is called even if the method does exist
• __dict__ = contains all the attributes that describe an object

 
Reinforcement Learning – learns actively, not just given correct instructions
Evaluative feedback – tells how good action was. -> function optimisation (evolutionary methods) Depends entirely on action taken (supervised learning = independent of action)

N-armed bandit problem. Task = maximise the reward, two options: exploitation, choosing the current known maximum, ‘greedy action’, or exploration, which may have higher reward but has uncertainty. Conflict between the choices.

Estimating action values: can be estimated by taken action a large number of times and taking mean (law of large numbers, sample average -> real average)

Greedy (always choose known optimum) vs e-greedy methods (choose known optimum but explore a small probability of times)

Deterministic = no randomness involved. A given input will always give the same output.

Monte Carlo – sample and average returns for each state-action pair, similar to bandit methods. Estimation method that involves averaging over many random samples of actual returns

1.	“Of course, if there are very many states, then it may not be practical to keep separate averages for each state individually. Instead, the agent would have to maintain vπ and qπ as pa- rameterized functions and adjust the parameters to better match the observed returns. This can also produce accurate estimates, although much depends on the nature of the parameterized function approximator (Chapter 9)”. [p71]
Note: vπ = value of state s given policy, qπ = value of state s given policy given an action


Nonassociative task – single best action in a stationary task, or best action as it changes over time with a nonstationary task
Associative search – more than one situation. Combines trial and error to find best action for situation, and also association of situation with which action is best suited to that situation
Full reinforcement learning: actions affect not just immediate reward, but the next situation as well

Nonstationary problem = optimal action value is changing (unconditional joint probability distribution is changing, and mean and variance)

General Policy Iteration (GPI) – interaction of policy evaluation and improvement

Dynamic Programming – given perfect model of environment as Markov decision process (MDP), what is optimal policy

Bellman optimality?
vπ(s)  = value of state s under policy π 
State value function:
 
Eπ = expected value of random variable given policy π, t = any time step, 
Qπ = Expected value of taking action a in state s under policy π
Note: gamma = the discount factor, difference in importance between future and present rewards
Finite Markov Decision Processes
Learner/decision maker = agent who selects actions, thing it interacts with = environment which gives rise to rewards
Task = one instance of reinforcement learning problem (eg. One order in atom = 1 task?)
Agent and environment interact at each of a sequence of discrete time steps, selects an action based on the state at that time (based on what actions are available in that state at time = t). Then at time t=t+1, receives a reward Rt+1, and is in new state St+1.
 “At each time step, the agent implements a mapping from states to prob- abilities of selecting each possible action. “  But where do these probabilities derive from??
NOTE: these time steps don’t need to be real time, they can be stages of decision making
Bellman equation: Says that value of start state = discounted value of expected next state + expected reward along the way
Hidden Markov Model?

• Q learning
Algorithms that don't learn the state-transition probability function are called model-free. One of the main problems with model-based algorithms is that there are often many states, and a naïve model is quadratic in the number of states. That imposes a huge data requirement.
Q-learning is model-free. It does not learn a state-transition probability function.
Also doesn’t use behaviour policy when selecting an action, but uses greedy policy every time. (in this way it is different from SARSA. Read more about difference here: https://stackoverflow.com/questions/6848828/reinforcement-learning-differences-between-qlearning-and-sarsatd)
 
 
Transition probabilities still exist, they are just not learned. “We assume that the transition function is deterministic for our calculation. Meaning if you take the same action from the same state, you will arrive in the same next state”
 iterative method where we are estimating the optimal action-value function without knowing the full dynamics of the environment and more specifically the value of p(s|s′,a)p(s|s′,a). If you happen to have a model of the environment that gives you this information you can change the update to include it by simply changing the return to γp(S′|S,A)maxa(Q(S′,a))γp(S′|S,A)maxa(Q(S′,a)).
See here: https://stats.stackexchange.com/questions/252261/why-there-is-no-transition-probability-in-q-learning-reinforcement-learning

 

Learn about design principles:

•	Principle of least astonishment (don’t be astonishing).
•	Make common things easy, and rare things possible
•	Consistency. One thing has become very clear to me, especially because of Python: the more random rules you pile onto the programmer, rules that have nothing to do with solving the problem at hand, the slower the programmer can produce. And this does not appear to be a linear factor, but an exponential one.
•	Law of Demeter: a.k.a. “Don’t talk to strangers.” An object should only reference itself, its attributes, and the arguments of its methods. This may also be a way to say “minimize coupling.”
•	Independence or Orthogonality. Express independent ideas independently. This complements Separation, Encapsulation and Variation, and is part of the Low-Coupling-High-Cohesion message.
•	Managed Coupling. Simply stating that we should have “low coupling” in a design is usually too vague - coupling happens, and the important issue is to acknowledge it and control it, to say “coupling can cause problems” and to compensate for those problems with a well-considered design or pattern.
•	Subtraction: a design is finished when you cannot take anything else away [5].
•	Simplicity before generality [6]. (A variation of Occam’s Razor, which says “the simplest solution is the best”). A common problem we find in frameworks is that they are designed to be general purpose without reference to actual systems. This leads to a dizzying array of options that are often unused, misused or just not useful. However, most developers work on specific systems, and the quest for generality does not always serve them well. The best route to generality is through understanding well-defined specific examples. So, this principle acts as the tie breaker between otherwise equally viable design alternatives. Of course, it is entirely possible that the simpler solution is the more general one.
•	Reflexivity (my suggested term). One abstraction per class, one class per abstraction. Might also be called Isomorphism.
•	Once and once only: Avoid duplication of logic and structure where the duplication is not accidental, ie where both pieces of code express the same intent for the same reason.

-	






