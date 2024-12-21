permisson_chart = {
        "pc_default_run": ("TR_SERVICE_RUN",),
        "pc_default_light": ("pc_default_run", "TR_ISSUE_ALLOW"),
        "pc_default": ("pc_default_light", "TR_SELF_TASK_SPECTATE", "TR_SELF_ASSIGNED_ACTION", "TR_TASK_ANY_TRANSFER_DENY"),
        "pc_default_team": ("pc_default", "TR_TEAM_TASK_WORKING"), #MUST TEAM ROLE! MUST TEAM_ID!
        "pc_default_team_opr": ("pc_default_team", "TR_TEAM_TASK_ADMIN"), #MUST TEAM_OPR ROLE! MUST TEAM_ID!
        "pc_default_team_adm": ("pc_default_team", "pc_spc_team_yoda"),  # MUST TEAM_ADM ROLE! MUST TEAM_ID!
        "pc_spc_usr_adm": ("TR_USER_ALL_MASTER",),
        "pc_spc_usr_team_adm":  ("TR_USER_TEAM_MASTER",), #MUST TEAM ROLE! MUST TEAM_ID!
        "pc_spc_team_yoda": ("pc_spc_usr_team_adm", "TR_TEAM_TASK_ADMIN"),  # MUST TEAM_ADM ROLE! MUST TEAM_ID!
        "pc_spc_project_yoda": ""
    }
 
 
def pc_role_unpacker_dc(self, dcs, pre_data=None, i=0, rr=None):
    permission_list = []
    permission_list_depends = []
    pc_main_roles = list(permit().permisson_chart.keys())
    for dc in dcs:
        dc_data = permit().permisson_chart[dc]
        print(f"DC= {dc}, DC_DATA= {dc_data}")
        for _dc_data in  dc_data:
            if str(_dc_data).startswith("pc_"):
                if _dc_data in pc_main_roles:
                    permission_list_depends.append(_dc_data)
                else:
                    pass
            else:
                permission_list.append(_dc_data)
    if rr is not None:
        if rr in permission_list:
            return True

    if pre_data is not None:
        for pre in pre_data:
            permission_list.append(pre)

    if permission_list_depends !=[]:
        self.pc_role_unpacker_dc(dcs=permission_list_depends, pre_data=permission_list, i=i + 1)
    else:
        print(f'\nITERATIO: — {i}\nXC: {permission_list}\nXC_ROLES: {permission_list_depends}')
        return permission_list



def pc_role_unpacker(self, req_role):
    pc_main_roles = list(permit().permisson_chart.keys())
    role_data = permit().permisson_chart[req_role]
    dcs = []
    for rc in role_data:
        if rc in pc_main_roles:
            dcs.append(rc)
    data = self.pc_role_unpacker_dc(dcs)
    print(f'XC_RETURNED: {data}')
    
def permit():
    pass

if __name__ == "__main__":
    permit()