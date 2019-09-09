import myfuncs
import json
import csv
import datetime


def write_data_to_json():
    ans = myfuncs.get_all_repos()
    # print(len(ans))
    repos = []
    pop_langs = ['JavaScript', 'Java', 'Python', 'C#', 'PHP', 'C++', 'C', 'TypeScript', 'Ruby', 'Swift']
    for item in ans:
        today = datetime.date.today()
        createdAt = datetime.date(int((item["createdAt"])[0:4]), int((item["createdAt"])[5:7]),
                                  int((item["createdAt"])[8:10]))
        updatedAt = datetime.date(int((item["updatedAt"])[0:4]), int((item["updatedAt"])[5:7]),
                                  int((item["updatedAt"])[8:10]))
        pop_lang = False
        if item["primaryLanguage"]:
            lang = item["primaryLanguage"]["name"]
            if lang in pop_langs:
                pop_lang = True
        else:
            lang = " "
        data = {
            "name": item["name"],
            "createdAt": (item["createdAt"])[:10],
            "updatedAt": (item["updatedAt"])[:10],
            "releases": item["releases"]["totalCount"],
            "primaryLanguage": lang,
            "mergedPullRequests": item["pullRequests"]["totalCount"],
            "closedIssues": item["closedIssues"]["totalCount"],
            "totalIssues": item["totalIssues"]["totalCount"],
            "closedVsTotalIssues": round((item["closedIssues"]["totalCount"]/item["totalIssues"]["totalCount"]), 3)
            if item["totalIssues"]["totalCount"] > 0 else 0,
            "daysSinceLastUpdate": (today - updatedAt).days if (today - updatedAt).days >= 0 else 0,
            "repoAgeInDays": (today - createdAt).days,
            "popularLanguage": pop_lang
        }
        repos.append(data)
    with open("repo_data.json", "w") as f:
        json.dump(repos, f, indent=4)


def from_json_to_csv():
    with open("repo_data.json", "r") as f:
        repos = json.load(f)
    # print(json.dumps(repos, indent=4))
    output = open("repo_data.csv", "w")
    out_csv = csv.writer(output)
    out_csv.writerow(repos[0].keys())
    for row in repos:
        out_csv.writerow(row.values())
    medianas = [int((len(repos)/2) - 1), int(len(repos)/2)]

    orderedByRAID = sorted(repos, key=lambda k: k["repoAgeInDays"])
    medianaRAID = round(((orderedByRAID[medianas[0]]["repoAgeInDays"] +
                          orderedByRAID[medianas[1]]["repoAgeInDays"])/2), 2)

    orderedByMPR = sorted(repos, key=lambda k: k["mergedPullRequests"])
    medianaMPR = round(((orderedByMPR[medianas[0]]["mergedPullRequests"] +
                         orderedByMPR[medianas[1]]["mergedPullRequests"])/2), 2)

    orderedByReleases = sorted(repos, key=lambda k: k["releases"])
    medianaReleases = round(((orderedByReleases[medianas[0]]["releases"] +
                              orderedByReleases[medianas[1]]["releases"])/2), 2)

    orderedByDSLU = sorted(repos, key=lambda k: k["daysSinceLastUpdate"])
    medianaDSLU = round(((orderedByDSLU[medianas[0]]["daysSinceLastUpdate"] +
                          orderedByDSLU[medianas[1]]["daysSinceLastUpdate"])/2), 2)

    orderedByCVTI = sorted(repos, key=lambda k: k["closedVsTotalIssues"])
    medianaCVTI = round(((orderedByCVTI[medianas[0]]["closedVsTotalIssues"] +
                          orderedByCVTI[medianas[1]]["closedVsTotalIssues"])/2), 2)

    num_repo_pop_langs = len(list(filter(lambda x: x["popularLanguage"] is True, repos)))

    metricas = {
        "medianaRAID": medianaRAID,
        "medianaMPR": medianaMPR,
        "medianaReleases": medianaReleases,
        "medianaDSLU": medianaDSLU,
        "totalRepPopLang": num_repo_pop_langs,
        "medianaCVTI": medianaCVTI
    }

    # print(json.dumps(metricas, indent=4))
    with open("respostas1-6.json", "w") as f:
        json.dump(metricas, f, indent=4)


def questao_7():
    pop_langs = []
    non_pop_langs = []
    with open("repo_data.json", "r") as f:
        repos = json.load(f)
    for repo in repos:
        if repo["popularLanguage"] is True:
            pop_langs.append(repo)
        else:
            non_pop_langs.append(repo)
    # print(len(pop_langs), len(non_pop_langs))
    mPopLangs = [int((len(pop_langs)/2) - 1), int(len(pop_langs)/2)]

    orderedByMPR = sorted(pop_langs, key=lambda k: k["mergedPullRequests"])
    medianaMPR_PL = round(((orderedByMPR[mPopLangs[0]]["mergedPullRequests"] +
                         orderedByMPR[mPopLangs[1]]["mergedPullRequests"]) / 2), 2)

    orderedByReleases = sorted(pop_langs, key=lambda k: k["releases"])
    medianaReleases_PL = round(((orderedByReleases[mPopLangs[0]]["releases"] +
                              orderedByReleases[mPopLangs[1]]["releases"]) / 2), 2)

    orderedByDSLU = sorted(pop_langs, key=lambda k: k["daysSinceLastUpdate"])
    medianaDSLU_PL = round(((orderedByDSLU[mPopLangs[0]]["daysSinceLastUpdate"] +
                          orderedByDSLU[mPopLangs[1]]["daysSinceLastUpdate"]) / 2), 2)

    metricas_PL = {
        "medianaMPR": medianaMPR_PL,
        "medianaReleases": medianaReleases_PL,
        "medianaDSLU": medianaDSLU_PL,
    }

    mNonPopLangs = [int((len(non_pop_langs) / 2) - 1), int(len(non_pop_langs) / 2)]

    orderedByMPR = sorted(non_pop_langs, key=lambda k: k["mergedPullRequests"])
    medianaMPR_NPL = round(((orderedByMPR[mNonPopLangs[0]]["mergedPullRequests"] +
                             orderedByMPR[mNonPopLangs[1]]["mergedPullRequests"]) / 2), 2)

    orderedByReleases = sorted(non_pop_langs, key=lambda k: k["releases"])
    medianaReleases_NPL = round(((orderedByReleases[mNonPopLangs[0]]["releases"] +
                                  orderedByReleases[mNonPopLangs[1]]["releases"]) / 2), 2)

    orderedByDSLU = sorted(non_pop_langs, key=lambda k: k["daysSinceLastUpdate"])
    medianaDSLU_NPL = round(((orderedByDSLU[mNonPopLangs[0]]["daysSinceLastUpdate"] +
                              orderedByDSLU[mNonPopLangs[1]]["daysSinceLastUpdate"]) / 2), 2)

    metricas_NPL = {
        "medianaMPR": medianaMPR_NPL,
        "medianaReleases": medianaReleases_NPL,
        "medianaDSLU": medianaDSLU_NPL,
    }

    with open('resposta7.txt', 'w') as f:
        f.write("Dados de repositórios cuja linguagem principal é popular (está no top 10 do enunciado):\n\n")
        json.dump(metricas_PL, f, indent=4)
        f.write("\n\nDados de outros repositórios:\n\n")
        json.dump(metricas_NPL, f, indent=4)


if __name__ == '__main__':
    # write_data_to_json()    # ideia: executar poucas vezes, para nao estourar o limite de requisicoes
    from_json_to_csv()      # ideia: usar o json aqui salvo das requisicoes para escrever o csv
    questao_7()
