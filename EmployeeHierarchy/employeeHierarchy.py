class Employee(object):
    def __init__(self, name):
        self.name = name
        self.manager = None
        self.directs = []


class EmployeeHierarchy(object):
    def __init__(self):
        self.rootTracking = set()
        self.tree = dict()  # key: employee name, value is the employee object
        
    def add_emp_mgr_relationship(self, emp, mgr):
        # for both the employee and manager, create a node in the tree
        # if needed
        if (emp.name not in self.tree):
            self.tree[emp.name] = emp

        if (mgr.name not in self.tree):
            self.tree[mgr.name] = mgr

        # once added to the three, add the relationship b/w the two nodes
        emp.manager = mgr
        mgr.directs.append(emp)
            
    def print_hierarchy(self):
        # find the root, the employee w/ no manager
        root = None

        for key in self.tree.keys():
            if (self.tree[key].manager is None):
                root = self.tree[key]
                break

        self.print_hierarchy_helper(root)

    # do a pre-order traversal of the tree
    def print_hierarchy_helper(self, node, depth=0):
        for x in range(depth):
            print("-", end="")

        print("> " + node.name)

        for directReport in node.directs:
            self.print_hierarchy_helper(directReport, depth + 1)


eHier = EmployeeHierarchy()
empZ = Employee("Z")
empX = Employee("X")
empY = Employee("Y")
empA = Employee("A")
empB = Employee("B")
empC = Employee("C")
empD = Employee("D")


eHier.add_emp_mgr_relationship(empX, empZ)
eHier.add_emp_mgr_relationship(empY, empZ)

eHier.add_emp_mgr_relationship(empA, empX)
eHier.add_emp_mgr_relationship(empB, empX)

eHier.add_emp_mgr_relationship(empC, empY)
eHier.add_emp_mgr_relationship(empD, empY)

eHier.print_hierarchy()

input("Enter to exit...")
