__author__ = 'burt'
"""
when scrapers retrieve a username, they feed it to this class
"""
class Username_Store(object):
    def __init__(self, output_file):
        self.output_file = output_file
        # this class maintains a map from domains to lists of username strings
        self.usernames = {}

    def store_username(self, username, domain):
        # usernames are guaranteed to be unique on a domain.
        if domain in self.usernames:
            self.usernames[domain].append(username)
        else:
            self.usernames[domain] = [username]

    def save_usernames(self):
        f = open('w')
        for domain in self.usernames:
            print 'writing %d usernames from domain %s' % (self.usernames[domain].length, domain)
            f.writeline('#' * 10)
            f.writeline(domain + '\n')
            for username in self.usernames[domain]:
                f.writeline(username + '\n')

        f.close()

    def count_usernames(self):
        username_count = 0
        for domain in self.usernames:
            username_count += len(self.usernames[domain])
        return username_count