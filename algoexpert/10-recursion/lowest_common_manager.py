def lowest_common_manager(root_manager, report_one, report_two):
    return get_org_info(root_manager, report_one, report_two).lowest_common_manager

def get_org_info(node_master, node_child_one, node_child_two):
    num_important_reports = 0
    for report in node_master.report:
        org_info = get_org_info(report, node_child_one, node_child_two)

        if org_info.lowest_common_manager is not None:
            return org_info

        num_important_reports += org_info.num_important_reports
    
    if manager == node_child_one or manager == node_child_two:
        num_important_reports += 1

    lowest_common_manager = manager if num_important_reports == 2 else None
    return Org_info(lowest_common_manager, num_important_reports)

class Org_info:
    def __init__(self, lowest_common_manager, num_important_reports):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports

