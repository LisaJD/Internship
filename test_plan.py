#!/ms/dist/python/PROJ/core/2.7.9-64/bin/python #first specify version of python
import sys, ms.version
ms.version.addpkg('python', 'ng-trunk', meta='ets') # installs the est/python/ng package, access to libraries implementing testplan framework

import ets
from ets.testplan import test_plan
from ets.testcases.multitest import MultiTest
from est.testcases.multitest.suite import testsuite, testcase

@testsuite( tags = 'tagA') # suite contains tests often across multiple files
class BasicSuite(object):
    @testcase( parameters=(
        (2, 2),(1, 3) # can have multiple parameters passed to same testcase, will run a test for each of these subbed as a and b
        tags = 'tagA' # tests can be tagged, so that tests can be filtered to only run one tag group at runtime
    ))
    def test_example(self, env, result, ): #result = provides access to test report and assertions such as equals()
        result.equal(4, description='Expect 4') (a + b, name='should equal 4') #first argument = expected result and its description
    `   # second argument = calculated result and label 

@test_plan(name='Basic', description='A first test') # mark the main function as a test plan

def main(plan, parser)
    plan.add(MultiTest(name='Name', description='Description', suites=BasicSuite(), environment=[ ])) # main function acts as entry point, holds instance of test framework being used (here MultiTest)
    # can run multiple test suites (put in square brackets)
if __name__ == '__main__':
    main()
    
    
    e='Name', description='Description', suites=BasicSuite(), environment=[ ])) # main function acts as entry point, holds instance of test framework being used (here MultiTest)    # can run multiple test suites (put in square brackets)

if __name__ == '__main__':

    main()


