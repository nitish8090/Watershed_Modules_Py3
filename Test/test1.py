groups = {'Drought': ['Rel_P_DROUGHT.png', 'Res_P_DROUGHT.png', 'RRV_P_DROUGHT.png', 'Vul_P_DROUGHT.png'],
          'GW': ['Rel_PERC_GW.png', 'Res_PERC_GW.png', 'RRV_PERC_GW.png', 'Vul_PERC_GW.png'],
          'PET': ['Rel_PET.png', 'Res_PET.png', 'RRV_PET.png', 'Vul_PET.png'],
          'SURQ_HIGH': ['Rel_SURQ_HIGH.png', 'Res_SURQ_HIGH.png', 'RRV_SURQ_HIGH.png', 'Vul_SURQ_HIGH.png'],
          'SYLD': ['Rel_SYLD.png', 'Res_SYLD.png', 'RRV_SYLD.png', 'Vul_SYLD.png'],
          'WHI': ['Rel_WHI.png', 'Res_WHI.png', 'WHI.png', 'Vul_WHI.png']}

for key in groups.keys():
    l = []
    i = len(groups[key]) - 1
    while i >= 0:
        l.append(groups[key][i])
        i -= 1
    print(l)

a = {'Drought': ['RRV_P_DROUGHT.png', 'Vul_P_DROUGHT.png', 'Res_P_DROUGHT.png', 'Rel_P_DROUGHT.png'],
     'GW': ['RRV_PERC_GW.png', 'Vul_PERC_GW.png', 'Res_PERC_GW.png', 'Rel_PERC_GW.png'],
     'PET': ['RRV_PET.png', 'Vul_PET.png', 'Res_PET.png', 'Rel_PET.png'],
     'SURQ_HIGH': ['RRV_SURQ_HIGH.png', 'Vul_SURQ_HIGH.png', 'Res_SURQ_HIGH.png', 'Rel_SURQ_HIGH.png'],
     'SYLD': ['RRV_SYLD.png', 'Vul_SYLD.png', 'Res_SYLD.png', 'Rel_SYLD.png'],
     'WHI': ['WHI.png', 'Vul_WHI.png', 'Res_WHI.png', 'Rel_WHI.png']}
