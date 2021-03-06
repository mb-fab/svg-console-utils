#!/usr/bin/python
#
# Library to handle SVG path descriptions and segments
#

class Segment:
    #
    # parse segment from string
    #
    def __init__(this, s, a=None, b=None):
        s = s.strip()

        this.type = s[0]

        if a != None:
            # explicit intialization
            this.x = a
            this.y = b

        elif "mMlL".find(this.type) > -1:
            # parse from string
            c = s.split(" ")[1].split(",")
            this.x = float(c[0])
            this.y = float(c[1])

    #
    # convert segment back to string
    #
    def __str__(this):
        if "mMlL".find(this.type) > -1:
            return this.type + " " + str(this.x) + "," + str(this.y)
        # else: return only the type
        return this.type

class D:
    #
    # initialize path data
    #
    def __init__(this, s=None):
        # initialize empty
        this.segments = []

        if s != None:
            s = s.strip()
            print "Parsing d: "+s
            # parser cursor
            p = 0
            while p < len(s):
                # search for beginning of next segment
                while (p < len(s)) and ("mMlLzZ".find(s[p]) == -1):
                    p += 1

                # what's there after one space?
                q = p + 2
                if (q < len(s)) and ("-0123456789".find(s[q]) != -1):
                    # has number arguments
                    e = s.find(" ", q)
                    if e < q:
                        # string does apparently not end with a space
                        e = len(s)
                    this.segments.append( Segment(s[p:e]) )
                    p = e + 1
                else:
                    # has no number args
                    this.segments.append( Segment(s[p:p+2]) )
                    p = q

    #
    # return number of segments in this path description
    #
    def __len__(this):
        return len(this.segments)

    #
    # export as string
    #
    def __str__(this):
        return " ".join([str(segment) for segment in this.segments])

    #
    # min/max functions
    #
    def min_x(this):
        result = None
        for segment in this.segments:
            if "ML".find(segment.type) > -1:
                if (result == None) or (segment.x < result):
                    result = segment.x
        return result

    def max_x(this):
        result = None
        for segment in this.segments:
            if "ML".find(segment.type) > -1:
                if (result == None) or (segment.x > result):
                    result = segment.x
        return result

    def min_y(this):
        result = None
        for segment in this.segments:
            if "ML".find(segment.type) > -1:
                if (result == None) or (segment.y < result):
                    result = segment.y
        return result

    def max_y(this):
        result = None
        for segment in this.segments:
            if "ML".find(segment.type) > -1:
                if (result == None) or (segment.y > result):
                    result = segment.y
        return result
