import Recommendations as Recs

def parseform(p1, p2, p3, p4, p5):

    pref = []
    if p1:
        pref.append(int(p1))
    if p2:
       pref.append(int(p2))
    if p3:
       pref.append(int(p3))
    if p4:
       pref.append(int(p4))
    if p5:
       pref.append(int(p5))

    return pref

def orderPrefs(order, pref):
    if order == 'Ascending':
        rec_list = Recs.StrategyRecommendationAsc(pref[0], pref[1], pref[2])
    else:
        rec_list = Recs.StrategyRecommendationDesc(pref[0], pref[1], pref[2])

    return rec_list.run_algorithm()