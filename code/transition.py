class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        id = conf.stack[-1]
        # s = conf._tokens[id]

        for (head, rel, child) in conf.arcs:
            if child == id:
                return -1

        if id!=0 :                               # or, s['address']!=0
            temp = conf.stack.pop(-1)
            conf.arcs.append((conf.buffer[0], relation, temp))
            # return conf
        else:
            return -1

        # raise NotImplementedError('Please implement left_arc!')
        # return -1

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))
        # return conf

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.stack :
            return -1

        id = conf.stack[-1]
        # s = conf._tokens[id]

        # print
        # print 'Hey there in (transition.py), s : {}'.format(s)
        # print

        status = False
        for (head, rel, child) in conf.arcs:
            if child == id and status==False:
                status=True

        if status==True:                   # The REDUCE transition pops the stack and is subject to the            
            temp = conf.stack.pop(-1)      # preconditions that the top token has a head.
            # return conf
        else:
            return -1

        # raise NotImplementedError('Please implement reduce!')
        # return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer :
            return -1

        id = conf.buffer.pop(0)
        conf.stack.append(id)
        # return conf

        # raise NotImplementedError('Please implement shift!')
        # return -1
