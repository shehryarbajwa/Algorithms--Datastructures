class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

###Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    if user in group.users:
        return True
    if len(group.groups) == 0:
        return False
    for subgroup in group.groups:
        return is_user_in_group(user, subgroup)

parent = Group('Bob')
child = Group('Bob_children')
sub_child = Group('Bob_Child_Thomas_children')
sub_child_child = Group('Richard_Children')

parent.add_group(child)
child.add_group(sub_child)
sub_child.add_group(sub_child_child)

parent_user = 'Bob'
parent.add_user(parent_user)

child_user = 'Thomas'
child.add_user(child_user)

sub_child_user = "Richard"
sub_child.add_user(sub_child_user)

sub_child_child_user = 'Sophia'
sub_child_child.add_user(sub_child_child_user)


##Tests
print( is_user_in_group( "Bob", parent ) )
#True
print( is_user_in_group( "Thomas", parent ) )
#True
print( is_user_in_group( "Richard", parent ) )
#True
print( is_user_in_group( "Sophia", parent ) )
#True
print( is_user_in_group( "Richard", sub_child_child ) )
#False
print( is_user_in_group( "Thomas", sub_child ) )
#False
print( is_user_in_group( "Thomas", sub_child_child ) )
#False
print( is_user_in_group( "Bob", sub_child_child ) )
#False
print( is_user_in_group( "Richard", sub_child_child ) )
#False