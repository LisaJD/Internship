
def check(expectation, observation, result):
  import ets
  for key, value in expectation.iteritems():
    exp = expectation.get(key)
    obs = observation.get(key) #gets the value pairs for each key in for loop
    print(len(obs), len(exp))
    if len(obs) != len(exp):
      result.fail("Oh no!") 
      return 0 
    else:
      for i in range(len(obs)): #this loop will not run if len(obs) == 0
        #unlike my code, this will work even if there is more than one message in client or exchange
        exp_msg = exp[i]
        obs_msg = obs[i]
        print(exp_msg, obs_msg)
        success = ets.testcases.multitest.result.dictmatch(result=result,
                                                verbose=result.verbose,
                                                reference=obs_msg,
                                                description=None,
                                                ignore=[],
                                                only=exp_msg,
                                                value=exp_msg) 
        print(success)
        if success == False:
          return 0   
    return 1
  
  


http://pyfixmsg.readthedocs.io/en/latest/api.html#fixmessage

observation = {'client': [{150: 0, 39:0}],
                'exchange':[] } #dict inside dict
expectation = {'client': [{150: 0}],
                'exchange':[] }

def check(expectation, observation):
    if expectation['client'] != []:
        x = expectation['client'][0]
        y = observation['client'][0]
        for key, value in x.items():
            if key in y and value == y[key]:
                continue
            else:
                return 0
    if expectation['exchange'] != []:
        a = expectation['exchange'][0]
        b = observation['exchange'][0]
        for key, value in a.items():
            if key in b and value == b[key]:
                continue
            else:
                return 0
    return 1


  
#add to simple function:
action, expectation = world.get_action()

#in get_action function:

return "client cancels order", CLIENT, co.cancel(), expectation 
#Note: the expectation can either be getting value from the dictionary of 
#'expected dictoinaries for reports that Chihang printed for me', or
#use debugger to look at the data inside co.cancel - does it give us the tag names which
#we can extract?

#need to find where the functions (client_order.)reject, amend, ack etc are defined
#trying importing all from file, then simple.__dict__? or __path__


