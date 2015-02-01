class Post(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        # print "POST Object attributes:"
        # print "========="
        # for var in vars(self):
        #     print var
        # print "ID: %s" % self.id
        # print "TITLE: %s" % self.post_title
        # print "DATE: %s" % self.post_date
        # print "STATUS: %s" % self.post_status
        # print "---------"


    def __iter__(self):
        return iter(self.__dict__)
