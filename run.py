# ------------------ Credits ----------------------- #
# Idea and exploit: Boxxy                            #
# Code, performance and functionality: Bermdingetje  #
# -------------------------------------------------- #
# Requirements: python2.7 and requests, oh and a brain :')

import sys

from bin import Handler
_Handler = Handler.MainFactory()


if __name__ == '__main__':
    user_id = raw_input("Target user(ID):")
    if user_id:
        user_id = int(user_id)
        print 'Starting to vote on target: {0}'.format(user_id)
        _Handler.run(user_id)
    else:
        print 'You forgot to give me an ID.'
        sys.exit()
