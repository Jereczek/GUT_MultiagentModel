import unittest

# pylint: disable=[import-error]

import context

from suswa.suswalib.agents.agent import *

class AgentUnitTests(unittest.TestCase):

    def selftest(self):
        self.assertTrue(True)

    def exists(self):
        a = Agent()
        pass

if __name__ == '__main__':
    unittest.main()